/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool rec(TreeNode* root, long max,long min){
        if (root==nullptr){return true;}
        if (root->left== nullptr && root->right == nullptr){return true;}
        if (root->left!= nullptr){
            if (root->val <= root->left->val || root->left->val <= min ){return false;}
        }
        if (root->right!= nullptr){
            if (root->val >= root->right->val ||root->right->val >=max){return false;}
        }
        return rec(root->left,root->val,min) && rec(root->right,max,root->val);
    
    }

    bool isValidBST(TreeNode* root) {
        return rec(root,LONG_MAX,LONG_MIN);
    }
};