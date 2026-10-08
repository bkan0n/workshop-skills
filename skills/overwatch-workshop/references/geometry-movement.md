# Geometry, targeting and movement

## Give vectors a role and space

Workshop uses one vector representation for positions, directions, displacement and velocity. Record the role and units before combining them. The documented axes are **+X left, +Y up, +Z forward**; local player origin is at the feet. A position's coordinate values do not imply a direction or velocity.

- Displacement from A to B is B − A; Vector Towards returns that displacement, while Direction Towards returns a normalized direction.
- Position Of uses world position at the player's feet; Eye Position is suitable for an aim ray. Camera Live Capture captures eye rather than foot position.
- Local Vector Of / World Vector Of use rotation for a direction or velocity, and **rotation plus translation for a position**. Translating a direction erroneously makes it depend on world location.
- A normalized direction multiplied by speed gives velocity; the magnitude of velocity gives speed. Several movement actions normalize Direction internally, so vector magnitude is not their speed control.

Angle helpers have an archived sign discrepancy: Direction From Angles describes positive vertical as up, while Vertical Facing Angle/Vertical Angle Towards describe positive as down. Do not assume an unchecked inverse pair. Test looking up/down with the exact conversion functions used. The advanced cross-product tutorial's `Forward × Right = Up` example conflicts with its component formula and the documented vectors: `(0,0,1) × (-1,0,0)` yields `(0,-1,0)`. Treat the example as disputed; do not copy it into a camera basis. Guard against parallel/zero basis vectors before normalization.

## Raycast construction and misses

A raycast ends at its explicit endpoint, even in empty air. Use `start + direction * range` when the intention is a ranged ray; passing a direction alone as End Position makes it a point near world origin. For player aiming, explicitly choose Eye Position, facing direction, intended range, included/excluded players and whether owned objects should block.

| Query | No-hit behavior in archived reference |
| --- | --- |
| Ray Cast Hit Position | Returns the requested end position |
| Ray Cast Hit Player | Returns Null when no player is hit |
| Ray Cast Hit Normal | Returns a direction from end back to start |

A returned position is not proof of a collision. An endpoint return can also coincide with a real hit exactly at that endpoint. Use Hit Player when the needed answer is player identity; interpret endpoint/normal sentinels for environment-hit logic and test the boundary case. Do not apply impact effects blindly to every returned endpoint.

Excluded players take precedence over included players. Phased Out players are ignored. A player passed directly as a ray position is documented to resolve **two meters above their feet**, so it is not generally equivalent to Position Of(player) or Eye Position(player). Owned-object toggles cover barriers/turrets. Is In View Angle is not an occlusion check and uses feet-based geometry; use line-of-sight/raycast explicitly when walls must matter. Nearest Walkable Position also requires spawn reachability; “nearest geometry” and “reachable walking surface” differ.

## Choose the movement mechanism

| Need | Mechanism and caveat |
| --- | --- |
| One instantaneous velocity change | Apply Impulse; direction normalizes; cancellation/velocity behavior depends on selected Impulse enum |
| Continued force-like acceleration | Start Accelerating; gravity/friction can prevent target speed; stop explicitly |
| Simulated directional input | Start Throttle In Direction; magnitude 1 is full input; choose replace versus add |
| Bound/prevent player's input | Start Forcing Throttle; minima can force movement, maxima can prevent it |
| Rotate/scale input for camera control | Start Transforming Throttle; scale axes before rotation; inputs update continuously |
| Exact placement over time | Start Forcing Player Position; reevaluation updates position but not selected Player |
| One reposition | Teleport; does not imply resetting all movement state |
| Parent-child movement | Attach Players; child cannot move freely until detached or teleported; many children may share one parent |

The newer Impulse reference distinguishes legacy XZ/Y cancellation from XYZ variants and velocity incorporation. Read the selected enum rather than using “cancel motion” as a universal description. Acceleration's archived horizontal cap and formula `Max Speed^2 - Rate/62.5` require targeted validation: the formula's interpretation is unclear, so do not build a precision controller from it uncritically.

Disabling environment collision leaves floors enabled unless Include Floors is true. Large scaled players in complex geometry can severely raise server load; disabling their environment collision trades collision behavior for performance. Start Camera continuously reads eye/look-at positions and needs Stop Camera cleanup. A custom camera does not automatically change movement input; use throttle transformation deliberately.

Offline source details: [geometry](wiki/geometry.md) and [input/movement](wiki/input-movement.md).

## Evidence

Archived snapshot **2026-09-29**: [vector guide](https://workshop.codes/wiki/articles/1903) (2023-06-11), [Vector](https://workshop.codes/wiki/articles/4758), [Direction Towards](https://workshop.codes/wiki/articles/4592), [Vector Towards](https://workshop.codes/wiki/articles/4759), [local](https://workshop.codes/wiki/articles/4687), [world](https://workshop.codes/wiki/articles/4766), [angle discrepancy](https://workshop.codes/wiki/articles/7747), [vertical angle](https://workshop.codes/wiki/articles/4762), [cross-product tutorial](https://workshop.codes/wiki/articles/1963), [raycast guide](https://workshop.codes/wiki/articles/1948), [position](https://workshop.codes/wiki/articles/4730), [player](https://workshop.codes/wiki/articles/4729), [normal](https://workshop.codes/wiki/articles/4728), [view angle](https://workshop.codes/wiki/articles/4660), [walkable position](https://workshop.codes/wiki/articles/4696), [Impulse behavior](https://workshop.codes/wiki/articles/8044), [acceleration](https://workshop.codes/wiki/articles/6022), [throttle](https://workshop.codes/wiki/articles/4456), [bounds](https://workshop.codes/wiki/articles/4451), [transformation](https://workshop.codes/wiki/articles/4457), [forced position](https://workshop.codes/wiki/articles/4449), [attachment](https://workshop.codes/wiki/articles/6165), [collision](https://workshop.codes/wiki/articles/4509), [scaling](https://workshop.codes/wiki/articles/9662). Sign/formula conflicts and numeric behavior are not locally game-tested.
