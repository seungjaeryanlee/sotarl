---
layout: page
title: Atari Bank Heist Environment
permalink: /envs/gym/atari/bank-heist/

redirect_from:
 - /envs/gym/atari-2600/bank-heist/
 - /env/gym/atari/bank-heist/
 - /env/gym/atari-2600/bank-heist/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/bank-heist.mp4' | absolute_url }}" type="video/mp4">
</video>

Bank Heist is a maze video game developed by 20th Century Fox for the Atari 2600.

Each level in Bank Heist is a maze-like city (similar to Pac-Man). The objective of the game is to rob as many banks as possible while avoiding the police. The player controls a car called the Getaway Car. The car has a limited amount of fuel, which can be refilled by changing cities. Robbing a bank will cause a cop car to appear, as well as another bank. Up to three cars can be present in a city at a time. Cars can be destroyed by dropping dynamite out the tail pipe of the Getaway Car (however, dynamite can also destroy the Getaway Car). The player starts out with four spare cars (lives). Lives are lost by running out of fuel, being hit by dynamite, or hitting a cop car. If the player can rob nine banks in one city, an extra car is earned.

The left and right difficulty switches alter how hard the game is. When the left difficulty switch is set to A, the cop cars are smarter in catching the Getaway Car; when it's set to B, enemy cars move in a more set pattern. When the right difficulty switch is set to A, the banks appear in random spots; when the switch is set to B, the banks appear in preset locations.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Bank_Heist_%28Atari_2600%29)*

## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
