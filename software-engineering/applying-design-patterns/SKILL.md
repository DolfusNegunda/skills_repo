---
name: applying-design-patterns
description: Select and apply the right design pattern to a recurring design problem without over-engineering — recognize the problem shape, choose a creational/structural/behavioral pattern that fits, prefer the simplest thing that works, and know when a pattern is not warranted. Use when the user asks "which design pattern fits", "how should I structure this", is drowning in conditionals/duplication, or is tempted to add a Factory/Strategy/Observer.
---

# Applying Design Patterns

## Scope
Choosing whether a design pattern applies to a specific problem, picking the one that
fits its shape, and applying it at the right dose. Covers the classic creational,
structural, and behavioral patterns and — just as much — when to use none.

## Purpose
Solve a recurring design tension with a proven structure that makes change cheaper,
while resisting the far more common failure: adding patterns a problem doesn't have yet.

## When to use this skill
- "Which pattern fits here / how should I structure this?"
- A recurring tension: swelling conditionals on a type, duplicated construction, rigid coupling that resists a known upcoming change.
- Tempted to reach for a Factory, Strategy, Observer, Adapter, or Decorator.

## When NOT to use this skill
- Routine feature work with no recurring design tension → [implementing-features](../implementing-features/SKILL.md).
- Cleaning up code smells without needing a named pattern → [refactoring-code](../refactoring-code/SKILL.md).
- Judging an existing design → [reviewing-architecture](../../review/reviewing-architecture/SKILL.md).

## Inputs
- The concrete problem and the change it must absorb (what varies, what stays fixed).
- The current code shape and where it hurts (the smell driving this).
- Constraints: language idioms, team familiarity, performance, testability.

## Outputs
- A recommendation: the pattern (or "no pattern — do X"), why it fits, and the minimal form.
- The alternative considered and why it lost; the trade-off accepted.

## Workflow
```
Progress:
- [ ] 1. State the problem and what actually varies
- [ ] 2. Confirm the tension is real and recurring, not hypothetical
- [ ] 3. Match the problem shape to a pattern category
- [ ] 4. Compare 2 candidate patterns; check the no-pattern baseline
- [ ] 5. Apply the minimal form; introduce the abstraction only where variation exists
- [ ] 6. Verify it reads simpler and the target change is now cheap
```

**Step 1 — Name what varies.** Patterns isolate change. Say precisely what differs
across cases (the algorithm? the created type? the traversal?) and what is stable. If
nothing varies, no pattern applies.

**Step 2 — Demand real, recurring tension.** Apply a pattern to a problem you *have*,
not one you *might* have. Duplication seen three times, or a change the requirements
actually mandate — not "we may need to swap databases someday."

**Step 3 — Match shape to category.** Creational = object construction varies (Factory,
Builder, Singleton). Structural = composing/adapting objects (Adapter, Decorator,
Facade, Composite). Behavioral = varying algorithm or communication (Strategy, Observer,
State, Template Method, Command). Let the shape pick the category (see Decision framework).

**Step 4 — Compare and baseline.** Line up two plausible patterns and the no-pattern
option. Often a first-class function, a dict/map dispatch, a plain conditional, or an
existing language feature beats a full pattern. Enums-with-behavior often beat State.

**Step 5 — Apply minimally.** Introduce exactly one seam at the axis of variation. Don't
add interfaces with a single implementation "for symmetry." Keep names domain-oriented,
not `AbstractFooFactoryImpl`.

**Step 6 — Verify.** The code should now read more simply *and* make the driving change
a small, local edit. If it reads worse, remove the pattern.

## Principles
- **A pattern is a response to a force, not a goal.** No force, no pattern.
- **Prefer the simplest mechanism that works.** Function > object > pattern > framework.
- **Isolate what varies; leave what's stable alone.** The abstraction goes exactly at the variation axis.
- **Rule of three.** Wait until duplication or variation appears ~three times before abstracting.
- **Composition over inheritance** — Strategy/Decorator usually beat deep class hierarchies.
- **Use the language's built-in version.** First-class functions, iterators, context managers, and enums subsume many GoF patterns; don't reimplement them.

## Decision framework
- **Swelling `if type == …` / `switch` on a kind?** → Strategy or polymorphism; map dispatch if simple.
- **Object built in many steps / many optional params?** → Builder (or a config object / defaults).
- **Object's behavior changes with its internal state?** → State (or an enum with behavior).
- **Need to react to changes in another object?** → Observer / pub-sub (or an event/callback).
- **Incompatible interface you don't own?** → Adapter. **Simplify a messy subsystem?** → Facade.
- **Add behavior to some instances at runtime?** → Decorator (not a subclass explosion).
- **Only one variant exists and no second is required?** → No pattern; inline it.

## Common mistakes
- **Speculative generality** — patterns for change that never comes ("just in case").
- **Singleton as a global** — hidden shared state that wrecks testability; prefer injection.
- **Pattern-name-driven design** — starting from "let's use Observer" instead of the problem.
- **Interface for a single implementation** — indirection with no second case behind it.
- **Deep inheritance** where composition/Strategy would be flatter and swappable.
- **Reinventing built-ins** — a hand-rolled Iterator/Command when the language already has one.

## Validation checklist
- [ ] The varying axis is named; the pattern's seam sits exactly on it.
- [ ] The tension is real and recurring, not hypothetical.
- [ ] A no-pattern baseline was considered and consciously rejected.
- [ ] The result reads simpler than before, not just "more OO."
- [ ] The driving change is now a small, local edit.
- [ ] No single-implementation interfaces or unused extension points added.

## Edge cases
- **Two competing patterns fit:** pick the one with fewer moving parts and better team familiarity.
- **Legacy code:** wrap with Adapter/Facade at the boundary rather than rewriting inward.
- **Performance-critical path:** a pattern's indirection may cost — measure before adding layers.
- **Team unfamiliarity:** a well-named plain solution beats a "correct" pattern nobody maintains.

## Related skills
- [refactoring-code](../refactoring-code/SKILL.md) — applying a pattern is often a refactor toward a seam.
- [implementing-features](../implementing-features/SKILL.md), [designing-apis](../designing-apis/SKILL.md).
- [reviewing-architecture](../../review/reviewing-architecture/SKILL.md), [reviewing-code](../../review/reviewing-code/SKILL.md).

## Examples
**Input:** "This function has a growing `if payment_type == 'card' … elif 'paypal' … elif 'crypto'` and it's spreading to three other functions."
**Output:** Real, recurring variation on payment type → **Strategy**. Define a `PaymentMethod` interface with `charge()/refund()`, one implementation per type, and select via a small registry/map. Removes the repeated conditionals and makes adding a method a single new class. Rejected: no-pattern (duplication already at three sites) and a base-class hierarchy (composition is flatter and testable). Singleton for the registry avoided — inject it.

## Automation opportunities
- Lint for smells that signal a missing pattern: high cyclomatic complexity, repeated type switches.
- Add an architecture-decision-record note when a pattern is introduced, so intent survives.
- Flag single-implementation interfaces and speculative abstractions in code review.
