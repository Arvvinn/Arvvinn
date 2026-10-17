# Arvvinn GitHub profile design

## Goal
Create a polished profile README on github.com/Arvvinn that makes the user's engineering work easy to discover through verifiable public projects.

## Direction
Use a midnight navy canvas, ice cyan and lavender accents, restrained technical typography, and bilingual project descriptions. The selected direction combines project storytelling with a small number of useful widgets. A statistics-heavy wall would overemphasize account size; a decorative banner alone would leave technical depth unexplained.

## Components
Custom SVG hero; four clickable project cards for FoodGlass, Harness Lab, Course Monitor and VoiceLog; a locally stored technology icon strip; an API-derived statistics/language card; light/dark contribution snakes.

## Data and updates
Only public owned non-fork repositories enter statistics. Primary language distribution counts repositories. GitHub Actions runs daily with the built-in repository token and commits generated images. External actions are pinned to verified commit hashes. Failed data fetches fail the update without overwriting the last committed widgets.

## Validation
Check public project descriptions against their READMEs, parse all SVG/XML and workflow YAML, validate image references, inspect the rendered desktop and mobile README, and verify the first remote workflow and profile rendering after publishing.

## Scope
Publish a new public Arvvinn/Arvvinn profile repository using the already authenticated matching GitHub account. Do not change other repositories, profile settings, or expose private repository data. Keep workflow documentation separate from profile copy.
