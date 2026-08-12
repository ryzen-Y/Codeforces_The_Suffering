import os
import re
import requests

README = "README.md"
CF_DIR = "codeforces"
URL = "https://codeforces.com/api/problemset.problems"


def get_problems():
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    data = response.json()

    if data["status"] != "OK":
        raise RuntimeError("Codeforces API returned an error.")

    problems = {}

    for p in data["result"]["problems"]:
        if "contestId" not in p or "index" not in p:
            continue

        problem_id = f'{p["contestId"]}{p["index"]}'

        problems[problem_id] = {
            "name": p["name"],
            "rating": p.get("rating"),
            "contest_id": p["contestId"],
            "index": p["index"],
        }

    return problems


def get_solved_files():
    files = []

    if not os.path.isdir(CF_DIR):
        return files

    for file in os.listdir(CF_DIR):
        name, ext = os.path.splitext(file)

        if ext.lower() in {".py", ".cpp", ".c", ".java"}:
            if re.fullmatch(r"\d+[A-Za-z]+", name):
                files.append(name)

    return sorted(set(files), key=lambda x: (int(re.match(r"\d+", x).group()), x))


def rating_bucket(rating):
    if rating is None:
        return "RATING_UNRATED"
    if rating <= 1000:
        return "RATING_800_1000"
    if rating <= 1300:
        return "RATING_1100_1300"
    if rating <= 1600:
        return "RATING_1400_1600"
    if rating <= 1900:
        return "RATING_1700_1900"
    return "RATING_2000_PLUS"


def rating_text(rating):
    return str(rating) if rating is not None else "Unrated"


def language_name(ext):
    return {
        ".py": "Python",
        ".cpp": "C++",
        ".c": "C",
        ".java": "Java",
    }.get(ext.lower(), ext.lstrip(".").upper())


problems = get_problems()
files = get_solved_files()

counts = {
    "RATING_800_1000": 0,
    "RATING_1100_1300": 0,
    "RATING_1400_1600": 0,
    "RATING_1700_1900": 0,
    "RATING_2000_PLUS": 0,
    "RATING_UNRATED": 0,
}

rows = []

for problem_id in files:
    problem = problems.get(problem_id)

    if not problem:
        print(f"Warning: {problem_id} was not found in the Codeforces problemset.")
        continue

    rating = problem["rating"]
    bucket = rating_bucket(rating)
    counts[bucket] += 1

    ext = os.path.splitext(
        next(
            file for file in os.listdir(CF_DIR)
            if os.path.splitext(file)[0] == problem_id
            and os.path.splitext(file)[1].lower() in {".py", ".cpp", ".c", ".java"}
        )
    )[1]

    filename = problem_id + ext

    rows.append(
        f'| {problem["contest_id"]}{problem["index"]} | '
        f'[{problem["name"]}](https://codeforces.com/problemset/problem/'
        f'{problem["contest_id"]}/{problem["index"]}) | '
        f'{rating_text(rating)} | '
        f'[{language_name(ext)}](codeforces/{filename}) |'
    )

table = "\n".join(rows)

with open(README, "r", encoding="utf-8") as f:
    readme = f.read()

readme = re.sub(
    r'<!-- START_PROBLEMS -->.*?<!-- END_PROBLEMS -->',
    f'<!-- START_PROBLEMS -->\n\n{table}\n\n<!-- END_PROBLEMS -->',
    readme,
    flags=re.S,
)

replacements = {
    "CF_COUNT": len(files),
    **counts,
}

for key, value in replacements.items():
    readme = re.sub(
        rf'<!-- {key} -->.*?<!-- END_{key} -->',
        f'<!-- {key} -->{value}<!-- END_{key} -->',
        readme,
    )

with open(README, "w", encoding="utf-8") as f:
    f.write(readme)

print("README updated successfully!")
