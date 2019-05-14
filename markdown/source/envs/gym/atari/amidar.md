---
layout: page
title: Atari Amidar Environment
permalink: /envs/gym/atari/amidar/

redirect_from:
 - /envs/gym/atari-2600/amidar/
 - /env/gym/atari/amidar/
 - /env/gym/atari-2600/amidar/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/amidar.mp4' | absolute_url }}" type="video/mp4">
</video>

As in Pac-Man, the player is opposed by enemies who kill on contact. The enemies gradually increase in number as the player advances from one level to the next, and their speed also increases. On odd-numbered levels, the player controls an ape (in some versions labeled "Copier"), and must collect coconuts while avoiding headhunters (labeled "Police" and "Thief"). On even-numbered levels, the player controls a paint roller (labeled "Rustler"), and must paint over each spot of the board while avoiding pigs (labeled "Cattle" and "Thief"). Each level is followed by a short bonus stage.

Whenever a rectangular portion of the board is cleared (either by collecting all surrounding coconuts, or painting all surrounding edges), the rectangle is colored in, and in the even levels, bonus points are awarded (In odd-numbered levels, the player collects points for each coconut eaten). When the player clears all four corners of the board, he is briefly empowered to kill the enemies by touching them (just as when Pac-Man uses a "power pill"). Enemies killed in this way fall to the bottom of the screen and revitalise themselves after a few moments.

The game controls consist of a joystick and a single button labeled "Jump," which can be used up to three times, resetting after a level is cleared or the player loses a life. Pressing the jump button does not cause the player to jump, but causes all the enemies to jump, enabling the player to walk under them.

Extra lives are given at 50,000 points, and per 80,000 scored up to 930,000; after that, no more lives.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Amidar)*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
