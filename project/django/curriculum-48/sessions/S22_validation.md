# S22 — Validation: unique, blank/null

## Goal

Make the API reject bad data with clear errors.

## Concept (5 min)

Model constraints vs Serializer.validate_
unique=True, blank vs null for strings/FKs

## Backend steps

- Unique title (or unique per user later)
- Custom validate_title
- Return 400 with field errors

## Frontend steps

- Show field errors under inputs

## Check

- [ ] Duplicate title returns 400
- [ ] UI shows which field failed

## Common bugs

- null=True without blank=True surprises for CharField
