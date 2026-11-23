"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "e024e6444c8b34c6ed8281876a40c509"
GRADE_HASH = "ea30f8f77798d70d43c19cf04514099376e0d5f64334276f3c72d84c0297b505"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
