#include <vector>

using namespace std;

int main()
{
    vector<int> scores;

    vector<int> scores(3, 0); // -> [0, 0, 0]

    scores.push_back(7); // list.append(7)
    scores.pop_back(); // list.remove(-1)
    scores.insert(scores.begin() + 1, 5);
    scores.erase(scores.begin() + 1);
    int first = scores.front();
    int last = scores.back();
    int sixth = scores[5];
    int seventh = scores.at(6);
    int scores_len = scores.size();
    bool is_empty = scores.empty();
    scores.clear();
}
