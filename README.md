# Asymmetric Intelligibility Calculator

Estimate how difficult it is to understand one language for speakers of a related language.

## Getting Started

Here's a simple way to get this project running:
1. make a local copy of the project (download, fork or clone)
2. navigate to the local directory
3. install the project: `pip3 install . --upgrade` 
4. run the project: `python3 project.py`

The project depends on Python and pip (see https://www.python.org/downloads/). It was developed with Python 3.6.4 on Mac OSX 10.13.4.

## Description

I'm working on a larger project about asymmetric intelligibility. I'd like to understand this concept better as I read through the research, so I'm taking a stab at running some calculations myself.

People who speak related languages have a chance of being able to understand each other without explicitly studying each other's language. The term for this is **mutual intelligibility**. From what I'm reading, the classic example comes from Scandinavia where Swedish, Danish and Norwegian speakers can intercommunicate. However, the situation isn't simple. Communication in some language pairs (like Swedish and Danish) is harder than others (like Swedish and Norwegian). In addition, communication going one way (Danish for a Swede) is not as readily understood as in reverse (Swedish for a Dane).

I've read of ways to compute this complex intelligibility landscape. Using insights from research, this project compares pairs of languages and calculates the intelligibility of one member of a pair of languages given the other language. For example: how understandable is Swedish given Norwegian?

The project expects to compare two language varieties at a time. It relies on relatedness, meaning the words to be compared are related cognates (like Norwegian "jeg" and Swedish "jag") or related borrowings (like "universitet" in both). The direction of the comparison matters. I've read papers that used both Levenshtein distances and conditional entropy to calculate asymmetric intelligibility. I intended to demonstrate both here, but I cut scope to the Levenshtein distance.

## Goals

I have two goals for this project:
1. showcase a way to estimate asymmetric intelligibility between languages
2. learn about quantifying asymmetric intelligibility

## Academic Basis

Actually, these formulas are not _directly_ calculating intelligibility, but you can read more about that along with other "academic" stuff below.

The research I've read takes a stab at quantifying intelligibility in a way that can be measured in both directions among different language/dialect pairs. Gooskens worked with Levenshtein distances for Scandinavian, and Moberg et al gave a formula for conditional entropy. I set out to play with both and see how they might predict intelligibility among language pairs.

The calculations set out to quantify the difference between the way words sound in a language given another language. This relates to intelligibility among Scandinavian languages, with the authors mentioned above showing their asymmetry calculations relate well to real-life intelligibility tests. For the purpose of this little project I'll casually take the results to stand in for intelligibility. A more rigorous investigator would do some more statistics to figure out how well measures in certain directions within certain language pairs match direct tests of intelligibility, since those are susceptible to factors beyond language structure like motivation and exposure.
