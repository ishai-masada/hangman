#include "stdio.h"

enum Day {
    SUNDAY,
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY
};

struct Report {
    enum Day day;
    int gross_revenue;
    int material_costs;
    int wages;
};

char *day_to_string(enum Day day) {
    switch (day)
    {
        case SUNDAY:
            return "Sunday";
        case MONDAY:
            return "Monday";
        case TUESDAY:
            return "Tuesday";
        case WEDNESDAY:
            return "Wednesday";
        case THURSDAY:
            return "Thursday";
        case FRIDAY:
            return "Friday";
        case SATURDAY:
            return "Saturday";
    }
}

int calc_profit(struct Report report)
{
    return report.gross_revenue - report.material_costs - report.wages;
}

void print_profit(struct Report report) {
    int daily_profit = calc_profit(report);
    printf("profit for %s: $%d\n", day_to_string(report.day), daily_profit);
}

int main()
{
    struct Report reports[] = {
        {SUNDAY, 54, 20, 10}, // Sunday
        {MONDAY, 9, 0, 10},   // Monday
        {TUESDAY, 63, 0, 10},  // Tuesday
        {WEDNESDAY, 36, 5, 10},  // Wednesday
        {THURSDAY, 93, 0, 20},  // Thursday
        {FRIDAY, 78, 0, 10},  // Friday
        {SATURDAY, 10, 0, 10}   // Saturday
    };

    int net_profit = 0;
    for (int i = 0; i >= 7; i++) {
        struct Report day = reports[i];
        net_profit += calc_profit(day);
    }

    printf("weekly profits: $%d\n", net_profit);
}

