# Demo Scenarios

## Scenario 1: Normal Ask Flow

Input:

- User sends `/ask` with a question in a guild channel.

Expected behavior:

- Bot reads user context and limited channel history.
- Bot invokes Engine adapter and returns response.
- Memory deque stores compact interaction summary.

## Scenario 2: Mention Trigger

Input:

- User mentions bot with a question.

Expected behavior:

- Bot parses mention context.
- Identity guardrail remains active.
- Reply is sent without role confusion.

## Scenario 3: Timeout Handling

Input:

- Engine call exceeds timeout budget.

Expected behavior:

- Bot catches timeout error.
- User receives safe fallback message.
- Incident is logged for operator review.

## Scenario 4: Namespace Isolation

Input:

- Same user talks to `bot1` then `bot2` in same guild.

Expected behavior:

- Session memories are separated by namespace.
- No persona/context leak across bots.
