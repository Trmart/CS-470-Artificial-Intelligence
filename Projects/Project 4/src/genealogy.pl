/*
# --------------------
# @file     genealogy.pl
# @author   Taylor Martin
# @date     June 2023
# @class    CS 470 Artificial Intelligence
# @project  Project 4 - Genealogy
# @brief    This program uses Prolog to create a family tree Knowledge Base (KB) 
            and answer queries about the family tree.
# --------------------
*/ 

/* King Of The Hill Genealogy KB Facts */

% parents of Hank
parent(cotton, hank).
parent(tilly, hank).

% parents of Peggy
parent(doc, peggy).
parent(maddy, peggy).

% parents of gh
parent(cotton, gh).
parent(didi, gh).


% parents of Hoyt
parent(doc, hoyt).
parent(maddy, hoyt).

% parents of Leanne
parent(jane, leanne).
parent(john, leanne).

% parents of Bobby
parent(hank, bobby).
parent(peggy, bobby).

% parents of Luanne
parent(hoyt, luanne).
parent(leanne, luanne).


% males in genealogy
male(bobby).
male(hank).
male(cotton).
male(hoyt).
male(doc).
male(john).
male(gh).

% females in genealogy
female(peggy).
female(luanne).
female(didi).
female(leanne).
female(maddy).
female(jane).



% King Of The Hill Genealogy KB Rules

mother(X, Y) :-
    parent(X, Y),
    female(X).

father(X, Y) :-
    parent(X, Y),
    male(X).

child(X, Y) :-
    parent(Y, X).

partner(X, Y) :-
    child(Z, X),
    child(Z, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandchild(X, Y) :-
    grandparent(Y, X).

grandfather(X, Y) :-
    grandparent(X, Y),
    male(X).

grandmother(X, Y) :-
    grandparent(X, Y),
    female(X).

paternalgrandfather(X, Y) :-
    father(X, Z),
    father(Z, Y).

maternalgrandfather(X, Y) :-
    father(X, Z),
    mother(Z, Y).

paternalgrandmother(X, Y) :-
    mother(X, Z),
    father(Z, Y).

maternalgrandmother(X, Y) :-
    mother(X, Z),
    mother(Z, Y).

greatgrandparent(X, Y) :-
    parent(P, Y),
    grandparent(X, P).

greatgrandchild(X, Y) :-
    greatgrandparent(Y, X).

son(X, Y) :-
    child(X, Y),
    male(X).

daughter(X, Y) :-
    child(X, Y),
    female(X).

granddaughter(X, Y) :-
    grandchild(X, Y),
    female(X).

grandson(X, Y) :-
    grandchild(X, Y),
    male(X).

ancestor(X, Y) :-
    parent(X, Y).

ancestor(X, Y) :-
    parent(Z, Y),
    ancestor(X, Z).

descendant(X, Y) :-
    ancestor(Y, X).

relative(X, Y) :-
    ancestor(Z, X),
    ancestor(Z, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

sister(X, Y) :-
    sibling(X, Y),
    female(X),
    X \= Y.

brother(X, Y) :-
    sibling(X, Y),
    male(X),
    X \= Y.

uncle(X, Y) :-
    brother(X, Z),
    child(Y, Z).

aunt(X, Y) :-
    sister(X, Z),
    child(Y, Z).

cousin(X, Y) :-
    grandparent(Z, X),
    grandparent(Z, Y),
    \+sibling(X, Y),
    X \= Y.

nephew(X, Y) :-
    aunt(Y, X),
    male(X);
    uncle(Y, X),
    male(X).

niece(X, Y) :-
    aunt(Y, X),
    female(X);
    uncle(Y, X),
    female(X).

stepchild(X, Y) :-
    parent(Z, X),
    partner(Z, Y),
    \+parent(Y, X).

stepfather(X, Y) :-
    stepchild(Y, X),
    male(X).

stepmother(X, Y) :-
    stepchild(Y, X),
    female(X).
