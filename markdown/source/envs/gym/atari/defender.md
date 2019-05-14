---
layout: page
title: Atari Defender Environment
permalink: /envs/gym/atari/defender/

redirect_from:
 - /envs/gym/atari-2600/defender/
 - /env/gym/atari/defender/
 - /env/gym/atari-2600/defender/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/defender.mp4' | absolute_url }}" type="video/mp4">
</video>

Defender is a two-dimensional side-scrolling shooting game set on the surface of an unnamed planet. The player controls a space ship as it navigates the terrain, flying either to the left or right. A joystick controls the ship's elevation, and five buttons control its horizontal direction and weapons. The object is to destroy alien invaders, while protecting astronauts on the landscape from abduction. Humans that are abducted return as mutants that attack the ship. Defeating the aliens allows the player to progress to the next level. Failing to protect the astronauts, however, causes the planet to explode and the level to become populated with mutants. Surviving the waves of mutants results in the restoration of the planet. Players are allotted three ships to progress through the game and are able to earn more by reaching certain scoring benchmarks. A ship is lost if it is hit by an enemy, or hit by an enemy projectile, or if a hyperspace jump goes wrong (as they randomly do). After exhausting all ships, the game ends.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Defender_(1981_video_game))*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
