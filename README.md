# README

A starting solution to [a kata from Codurance](https://github.com/midmandle/jlrkata)

## Approach
It uses the Builder pattern, or tries to, in order to build a complex configuration object.

To extend this, users will need to add Enums in the right place, translate them into text in the ConfigBuilder, and 
add the Enum to the correct `permissible_{x}`