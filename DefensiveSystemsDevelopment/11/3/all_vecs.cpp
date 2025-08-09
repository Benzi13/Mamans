#include "all_vecs.h"

void all_vecs::addVec(const named_vector &vec)
{
    vecs.push_back(vec);
}

my_vector all_vecs::getVecByName(const std::string &name) const
{
    for (const auto &named_vec : vecs)
    {
        if (named_vec.getName() == name)
        {
            return named_vec.getValue();
        }
    }
    throw std::runtime_error("Vector with name '" + name + "' not found.");
}

int main()
{

    all_vecs vectors;
    vectors.addVec(named_vector(1, 1234, 645, "David"));
    vectors.addVec(named_vector(4, 78, 99, "Dana"));
    vectors.addVec(named_vector(4, 5, 123, "Moshe"));
    vectors.addVec(named_vector(4, 34, 433, "Vered"));
    vectors.addVec(named_vector(4, 2, 76, "Mohammed"));
    vectors.addVec(named_vector(14, 52, 12, "Yasmin"));
    vectors.addVec(named_vector(41, 45, 63, "Ahmed"));
    vectors.addVec(named_vector(5, 1, 8, "Lucy"));
    vectors.addVec(named_vector(41, 25, 6, "Naftali"));
    vectors.addVec(named_vector(2, 2, 88, "Ayelet"));

    my_vector v = vectors.getVecByName("Vered");
    v.print_vector();

    return 0;
}