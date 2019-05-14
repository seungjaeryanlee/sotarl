---
layout: page
title: Atari Krull Environment
permalink: /envs/gym/atari/krull/

redirect_from:
 - /envs/gym/atari-2600/krull/
 - /env/gym/atari/krull/
 - /env/gym/atari-2600/krull/

nav:
 - name: Overview
   permalink: '#overview'
 - name: State of the Art
   permalink: '#state-of-the-art'
---


## Overview

<video autoplay muted loop controls>
  <source src="{{ 'assets/_pages/envs/gym/atari/krull.mp4' | absolute_url }}" type="video/mp4">
</video>

The game generally follows the plot of the movie, and takes place on four separate screens. The first level begins with the player, as Colwyn, at his wedding to Lyssa, which is interrupted by the extraterrestrial Slayers. The game continues to generate new Slayers for the player to fight until he is overwhelmed and Lyssa is abducted to the Black Fortress.

The player then traverses the Iron Desert on a Fire Mare, stocking up on Colwyn's magical throwing weapon, the Glaive (in the film there is only one), by pressing the button each time the horse rides over one.

The next level takes place in the lair of the Widow of the Web. The player is required to jump between moving threads of web, working their way upward towards the Widow at the top of the screen, while avoiding a giant spider. After completing this task, the Widow reveals the location of the Black Fortress, and the player again rides a Fire Mare through the Iron Desert to reach it. If the player fails to arrive at the given location at the correct time of day, according to a timer at the top of the screen, he loses a life and must return to the Widow to find out the Fortress's new location.

Upon reaching the Black Fortress, the player must penetrate the energy barrier surrounding Lyssa with the Glaive (of which the player has a limited number), while the Beast attempts to block the player's shots and hit him with fireballs. If the Glaive hits the Beast, or is not caught on the rebound by the player, that Glaive is lost. If all of the player's Glaives are lost, he is expelled from the Fortress and must return to the Widow of the Web level, discover the new location of the Black Fortress, and traverse the Iron Desert again.

If the player manages to break through the barrier surrounding Lyssa, she transforms into a fireball which the player can throw at the Beast. If the fireball hits, the player wins, and the game starts over at a higher level of difficulty.

*Description from [Wikipedia](https://en.wikipedia.org/wiki/Krull_(video_game))*


## State of the Art

### Human Starts

$human_table

### No-op Starts

$noop_table

### Normal Starts

$unspecified_table
