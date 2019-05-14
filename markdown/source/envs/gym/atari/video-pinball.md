---
layout: page
title: Atari Video Pinball Environment
permalink: /envs/gym/atari/video-pinball/

redirect_from:
 - /envs/gym/atari-2600/video-pinball/
 - /env/gym/atari/video-pinball/
 - /env/gym/atari-2600/video-pinball/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/video-pinball.mp4' | absolute_url }}" type="video/mp4">
</video>

Video Pinball is a loosesimulation of a pinball machine: ball shooter, flippers, bumpers and spinners. It includes a unique rollover bonus with an Atari Inc. logo on the playfield; hitting the logo four times results in an extra ball.

Most of the game play involves learning how to perform specific functions, such as launching the ball or activating the flippers, with the Atari joystick. Moving the joystick controller down pulls the pinball machine plunger back while pressing the joystick button shoots the ball into the playfield. The left and right flippers are activated by moving the joystick controller left or right. The ball can be nudged (as in nudging a table gently in real life) by holding down the joystick button and moving the controller in a particular direction.


*Description from [Wikipedia](https://en.wikipedia.org/wiki/Video_Pinball_(1980_video_game))*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
