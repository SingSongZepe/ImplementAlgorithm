
#include <functional>
#include <algorithm>
#include <iostream>
#include <set>
#include <gtest/gtest.h>
#include <tuple>
#include <cmath>

#define DEBUG 0

typedef long long LL;

struct Node
{
    uint32_t l, r;
    mutable LL val;

    Node(uint32_t l, uint32_t r, LL val) : l(l), r(r), val(val) {};

    bool operator < (const Node& node) const
    {
        return l < node.l;
    }
};

std::set<Node>::iterator split(std::set<Node>& st, uint32_t pos)
{
    auto left = st.lower_bound(Node(pos, 0, 0));
#if DEBUG
    std::cout << "val " << left->val << std::endl;    
#endif
    if (left->l == pos || left == st.end()) return left;
    left--;
    LL val = left->val; uint32_t l = left->l; uint32_t r = left->r;  
    st.erase(left);
    st.insert(Node(l, pos-1, val));
#if DEBUG
    std::cout << "pos " << pos << std::endl;  
#endif
    return st.insert(Node(pos, r, val)).first;
}

// l, r are both inclusive
void assign(std::set<Node>& st, uint32_t l, uint32_t r, LL x)
{
    auto left = split(st, l);
    auto right = split(st, r+1);

    st.erase(left, right);
    st.insert(Node(l, r, x));
}

// l, r are both inclusive
void add(std::set<Node>& st, uint32_t l, uint32_t r, LL x)
{
    auto left = split(st, l);
    auto right = split(st, r+1);
    
    while (left != right)
    {
        left->val += x;
        left++;
    }
}

// l, r are both inclusive
LL kth(std::set<Node>& st, uint32_t l, uint32_t r, uint32_t k)
{
    auto left = split(st, l);
    auto right = split(st, r+1);
    
    // <val, interval length>
    std::vector<std::tuple<LL, uint32_t>> vec; 
    while (left != right)
    {
        vec.push_back(std::make_tuple(left->val, left->r - left->l + 1));
        left++;
    }
    std::sort(vec.begin(), vec.end());

    uint32_t count = 0;
    for (auto vl = vec.begin(); vl != vec.end(); vl++)
    {
        count += (uint32_t)std::get<1>(*vl);
        if (count >= k)
        {
            return (LL)std::get<0>(*vl);
        }
    }
    
    return std::get<0>(*vec.end());
}

// l, r are both inclusive
LL sum_of_pow(std::set<Node>& st, uint32_t l, uint32_t r, int pow_x, int modulo)
{
    auto left = split(st, l);
    auto right = split(st, r);

    LL sum = 0;
    while (left != right)
    {
        sum = (LL)((left->r - left->l + 1) * std::pow(left->val, pow_x)) % modulo;
    }

    return sum;
}

void print_set(std::set<Node>& st)
{
    for (auto it = st.begin(); it != st.end(); it++)
    {
        std::cout << "l " << it->l << " r " << it->r << " val " << it->val << std::endl;
    }
}

TEST(TEST_node_sortable, test1)
{
    std::vector<Node> nodes;
    nodes.push_back(Node(1, 3, 2));
    nodes.push_back(Node(2, 5, 6));
    nodes.push_back(Node(0, 1, 3));

    for (const Node& node : nodes)
    {
        std::cout << node.l << " ";
    }

    std::sort(nodes.begin(), nodes.end());

    for (const Node& node : nodes)
    {
        std::cout << node.l << " ";
    }
}

TEST(TEST_FUNC, test_assign)
{
    return;
    std::cout << "test assign func" << std::endl;
    // input
    int n = 10;
    int m = 10;
    int seed = 7;
    int vmax = 9;

    int modulo = 1000000007;

    std::set<Node> st;

    std::srand(seed);

    for (int i = 0; i < n; i++)
    {
        st.insert(Node(i, i, std::rand() % vmax));
    }

#if DEBUG
    print_set(st);
#endif

    for (int j = 0; j < m; j++)
    {
        std::cout << j << std::endl;
        int op = std::rand() % 4;
        int l = std::rand() % n;
        int r = std::rand() % n;
        if (l > r) 
        {
            std::swap(l, r);
        };
#if DEBUG
        std::cout << "opl " << l << " opr "<< r << std::endl; 
#endif
        std::cout << "operate an assgin op" << std::endl;
        int x = std::rand() % vmax;

        assign(st, l, r, x);
    }

    print_set(st);
}

TEST(TEST_FUNC, test_kth)
{
    return;
    std::cout << "test assign func" << std::endl;
    // input
    int n = 10;
    int m = 10;
    int seed = 7;
    int vmax = 9;

    int modulo = 1000000007;

    std::set<Node> st;

    std::srand(seed);

    for (int i = 0; i < n; i++)
    {
        st.insert(Node(i, i, std::rand() % vmax));
    }

#if DEBUG
    print_set(st);
#endif
    print_set(st);
    for (int j = 0; j < m; j++)
    {
        int op = std::rand() % 4;
        int l = std::rand() % n;
        int r = std::rand() % n;
        if (l > r) 
        {
            std::swap(l, r);
        };
#if DEBUG
        std::cout << "opl " << l << " opr "<< r << std::endl; 
#endif
        std::cout << "operate an find kth num op" << std::endl;
        int k = std::rand() % (r - l + 1);
        LL res = kth(st, l, r, k);

        std::cout << "in the range " << l << "-" << r << ", the " << k << "th number is " << res << std::endl;
        
    }
}



TEST(TEST_MAIN, test1)
{
    // input
    int n = 10;
    int m = 10;
    int seed = 17;
    int vmax = 9;

    int modulo = 1000000007;

    std::set<Node> st;

    std::srand(seed);

    for (int i = 0; i < n; i++)
    {
        st.insert(Node(i, i, std::rand() % vmax));
    }
    for (int j = 0; j < m; j++)
    {
        int op = std::rand() % 4;
        int l = std::rand() % n;
        int r = std::rand() % n;
        if (l > r) 
        {
            std::swap(l, r);
        }
        if (op == 0) {
            std::cout << "operate an assgin op" << std::endl;
            int x = std::rand() % vmax;
        
            assign(st, l, r, x);
        }
        else if (op == 1)
        {
            std::cout << "operate an add op" << std::endl;
            int x = std::rand() % vmax;
        
            add(st, l, r, x);
        }
        else if (op == 2)
        {
            std::cout << "operate an find kth num op" << std::endl;
            int k = std::rand() % (r - l + 1);
            LL res = kth(st, l, r, k);

            std::cout << "the " << k << "th number is " << res << std::endl;
        }
        else
        {
            std::cout << "operate an sum up pow of l-r num op";
            int pow_x = std::rand() % n;

            LL res = sum_of_pow(st, l, r, pow_x, modulo);
            std::cout << "the sum of " << l << "-" << r << " num to the " << pow_x << " power is " << res << std::endl; 
        }
    }
}

int main(int argc, char** argv)
{
    std::cout << "Chtholly Tree" << std::endl;

    ::testing::InitGoogleTest(&argc, argv);  
    return RUN_ALL_TESTS();  

    return 0;
}