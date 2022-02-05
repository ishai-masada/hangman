#include "stdio.h"

/* enum Name { */
/*     SUPER_MARIO, */
/*     LUIGI, */
/*     PIKACHU, */
/*     YOSHI */
/* }; */


/* char *name_to_string(enum Name name) { */
/*     switch (name) */
/*     { */
/*         case SUPER_MARIO: */
/*             return "Super Mario"; */
/*         case LUIGI: */
/*             return "Luigi"; */
/*         case PIKACHU: */
/*             return "Pikachu"; */
/*         case YOSHI: */
/*             return "Yoshi"; */
/*     } */
/* }; */

enum Color {
    BLACK,
    BROWN,
    BLUE,
    GREEN
};

enum Occupation {
    PLUMBER,
    POOPER,
    BLOOPER,
    BEING_STOOPID,
};

struct Person {
    enum Color eye_color;
    enum Occupation occupation;
    int age;
    int height;
    char name[50];
};

char *color_to_string(enum Color color) {
    switch (color)
    {
        case BLACK:
            return "Black";
        case BROWN:
            return "Brown";
        case BLUE:
            return "Blue";
        case GREEN:
            return "Green";
    }
};

char *occupation_to_string(enum Occupation occupation) {
    switch (occupation)
    {
        case PLUMBER:
            return "Plumber";
        case POOPER:
            return "Pooper";
        case BLOOPER:
            return "Blooper";
        case BEING_STOOPID:
            return "Being Stoopid";
    }
};

char main() {
    struct Person people[] = {
        {BROWN, PLUMBER, 30, 5, "Super Mario"},
        {BROWN, PLUMBER, 30, 6, "Luigi"},
        {BLACK, BEING_STOOPID, 2, 1, "Pikachu"}
    };
    for (int i = 0; i < 3; i++) {
        struct Person person = people[i];
        printf("%s \n - Eye Color: %s\n - Occupation: %s\n - Age: %d\n",
            person.name, color_to_string(person.eye_color),
            occupation_to_string(person.occupation), person.age);
    };
}
