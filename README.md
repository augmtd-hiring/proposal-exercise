# AUGMTD engineering exercise: prepare the proposal

Thanks for taking the time. This is a small, open slice of the kind of work you'd do with us. Please
**do not spend about more than 2 hours**. We care about your judgment far more than polish, and choosing what to leave
out is part of the exercise.

## Getting started

1. Click **Use this template → Create a new repository** (top right of this page).
2. Create it in your own account and set it to **Private**. Please don't make your solution public.
3. Clone it and work there.

## Context

AUGMTD is a proactive AI work platform. Most AI tools wait to be asked; AUGMTD gets ahead of the work.
It connects to a person's email, calendar, meetings and documents, notices what needs them, and
prepares the next step for them to review and approve. Nothing goes out without a person's click.

It runs as private AI, hosted in the EU. Our users trust us with their clients' information, so three
principles hold in everything we build:

1. **The person approves.** We prepare; they decide and send.
2. **Prepared work is grounded.** Every fact traces back to where it came from.
3. **Data goes to a model only when it has to, and only what has to.**

## The ask

Sam, a partner at a small consulting firm, says:

> "Can you prepare the proposal for Northwind? Everything we know is in there somewhere."

In `data/` you'll find:

| Path | What it is |
|---|---|
| `context.json` | Who Sam is, the firm, the timezone, and what "now" is |
| `crm/deal.json`, `crm/contacts.csv` | The firm's CRM export for this deal and its contacts |
| `emails/thread.json` | The email thread with Northwind |
| `meetings/discovery_call.md` | Sam's notes from the discovery call |
| `knowledge/` | The firm's services, rate card, standard terms, its usual proposal template, and two past proposals for other clients |

**Build what you think AUGMTD should do with that request.**

We've deliberately left decisions to you. For example: which sources to trust when they disagree,
whether to use the template, what to ask Sam versus what to assume, how Sam should review what you
prepared, and what a model should and shouldn't see. Make the calls you think are right and explain
them.

Treat the data as real: it's spread across sources, it isn't always consistent, it contains personal
and confidential information, and not everything in it should be trusted.

## The minimum we need

We'll run your work on a **second, different scenario**: same folder layout, a different firm and
client, and some files may be missing. Please don't hard-code anything to this one.

Pick **one** language and delete the other stub:

    npm install && npm run analyze -- data/ out/      # TypeScript (src/analyze.ts)
    python analyze.py data/ out/                      # Python (analyze.py; list packages in requirements.txt)

Your command must write:

- `out/proposal.md`: the proposal as Sam would review it
- `out/sources.json`: for each factual claim (amounts, dates, scope, names, terms), where it came from:

  ```json
  { "claims": [
      { "claim": "Two half-day workshops",
        "sources": [ { "file": "emails/thread.json", "ref": "message 6" } ] }
  ] }
  ```

- `out/model_log.jsonl`: every request sent to a language model, exactly as sent, one JSON object per
  line. If you send nothing, leave it empty. We will read this file.

Anything else (an outline, questions for Sam, a summary of changes, a review step) is up to you. Put
it in `out/` too.

## Model setup

Use any OpenAI-compatible chat completions endpoint, configured only through environment variables
(see `.env.example`):

    LLM_BASE_URL   LLM_API_KEY   LLM_MODEL

We'll run your code against a different provider and model than yours, possibly a self-hosted one, so
avoid provider-specific features. One run should cost well under €0.50.

## DECISIONS.md

Short is good. Cover:

- the main decisions you made, and why
- **data handling**: what reaches the model, what doesn't, and why
- risks you noticed in the data or in your approach
- what you'd do next with more time

## On AI tools

Use them: Claude Code, Cursor, Copilot, whatever you normally work with. We do too. We care about how
you steer and check them. If you're comfortable sharing it, export your session(s) into `ai-log/`
(for example Claude Code's `/export`, or a Cursor chat export). It's optional, and it helps us see how
you work.

## What we're not looking for

A UI, a server, a database, deployment or perfect coverage. A command and files are enough. If you
think the review experience matters, describe it.

## Submitting

1. Make sure the command runs from a clean checkout, and push your work.
2. In your repository: **Settings → Collaborators → Add people → `alexcollignon`** (read access is
   enough).
3. Reply to our e-mail with your repository link, by the date we agreed.

We review the latest commit at the moment you send the link. Please keep the exercise and your solution
private.

## What happens next

If we move forward, we'll book a 45-minute conversation: you walk us through your choices, and we
extend the work together, live.

## A note on your work

This is an exercise, not product work. The data is synthetic, every name in it is invented, and we
won't use your code. Your solution stays yours.
