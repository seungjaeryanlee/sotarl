---
layout: page
title: Atari Up and Down Environment
permalink: /envs/gym/atari/up-n-down/

redirect_from:
 - /envs/gym/atari-2600/up-and-down/
 - /env/gym/atari/up-and-down/
 - /env/gym/atari-2600/up-and-down/
 - /envs/gym/atari/up-and-down/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/up-n-down.mp4' | absolute_url }}" type="video/mp4">
</video>

Up'n Down is a vertically scrolling game that employs a pseudo-3D perspective.[citation needed] The player controls a purple dune buggy that resembles a Volkswagen Beetle.[citation needed] The buggy moves forward along a single-lane path; pressing up or down on the joystick causes the buggy to speed up or slow down, pressing right or left causes the buggy to switch lanes at an intersection, and pressing the "jump" button causes the buggy to jump in the air. Jumping is required to avoid other cars on the road; the player can either jump all the way over them, or land on them for points.[citation needed]

To complete a round, the player must collect 10 colored flags by running over them with the buggy. If the player passes by a flag without picking it up, it will appear again later in the round. The roads feature inclines and descents that affect the buggy's speed, and bridges that must be jumped. A player loses a turn whenever the buggy either collides with another vehicle without jumping on it, or jumps off the road and into the grass or water.


*Description from [Wikipedia](https://en.wikipedia.org/wiki/Up%27n_Down)*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
