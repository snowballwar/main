// ConsoleApplication1.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>


int* countBits(int n, int* returnSize) {
    int* List = malloc(sizeof(int) * (n + 1));
    *returnSize = n + 1;
    for (int i = 0;i <= n;i++) {
        if(i == 0) {
            List[0] = 0;
        }
        else if (i % 2 == 1) {
            List[i] = List[(i - 1) / 2] + 1;
        }
        else {
            List[i] = List[i / 2];
        }    
    }
    return List;
}

 /*Definition for singly - linked list.*/
struct ListNode {
    int val;
    struct ListNode* next;
};

void ListNodeTraverse(struct ListNode *head)
{
    struct ListNode *cur = head;
    while (cur != NULL) 
    {
        printf("%d -> ", cur->val);
        cur = cur->next;
    }
}

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* cur = head;
    int cnt = 0;
    while (cur != NULL) {
        cnt = cnt + 1;
        cur = cur->next;
    }
    struct ListNode* node_dummy = malloc(sizeof(struct ListNode));
    node_dummy->val = 0;
    node_dummy->next = head;
    cur = node_dummy;
    for (int i = 0;i < cnt - n;i++) {
        cur = cur->next;
    }
    cur->next = cur->next->next;
    return node_dummy->next;
}

 /* Definition for a binary tree node. */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    };

struct TreeNode *newNode(int val) {
    struct TreeNode *temp = malloc(sizeof(struct TreeNode));
    temp->val = val;
    temp->left = temp->right = NULL;
    return temp;
}

void inorderTraverse(struct TreeNode *root) {
    if (root != NULL) {
        inorderTraverse(root->left);
        printf("%d -> ", root->val);
        inorderTraverse(root->right);
    }
}

struct TreeNode *insertIntoBST(struct TreeNode* root, int val, int *rec_cnt) {
    *rec_cnt = *rec_cnt + 1;
    if (root == NULL) {
        struct TreeNode *new_node = malloc(sizeof(struct TreeNode));
        new_node->val = val;
        new_node->left = new_node->right = NULL;
        return new_node;
    }
    if (val < root->val) {
        root->left = insertIntoBST(root->left, val, rec_cnt);
    }
    else {
        root->right = insertIntoBST(root->right, val, rec_cnt);
    }
    return root;
}

int maxPlanes(int *startHeight, int *descentRate, int n) {
    int* hitTime = malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        hitTime[i] = ceil((double)startHeight[i] / (double)descentRate[i]);
    }
    int res = n;
    for (int i = 0; i < n; i++) {
        if ((i + 1) > hitTime[i]) {
            res = i;
        }
    }
    return res;
}

//static void delete_item(struct mynode** root, int value) {
//
//    struct node* mynode = *root, *prev;
//
//    if (mynode != NULL && mynode->data == value) {
//        *root = mynode->next; 
//        free(mynode); 
//        return;
//    }
//
//    while (mynode != NULL && mynode->data != value) {
//        prev = mynode;
//        mynode = node->next;
//    }
//
//    if (mynode == NULL)
//        return;
//
//
//    prev->next = mynode->next;
//
//    free(mynode);
//}

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* removeElements(struct ListNode* head, int val) 
{
    struct ListNode* dummy_node = malloc(sizeof(struct ListNode));
    dummy_node->val = 0;
    dummy_node->next = head;
    struct ListNode* prev = malloc(sizeof(struct ListNode));
    prev = dummy_node;
    struct ListNode* cur = malloc(sizeof(struct ListNode));
    cur = head;
    while (cur != NULL)
    {
        if (cur->val == val)
        {
            prev->next = cur->next;
            cur = cur->next;
        }
        else
        {
            prev = cur;
            cur = cur->next;
        }
    }
    return dummy_node->next;
}

struct ListNode* removeElementsDpointer(struct ListNode** head, int val)
{
    struct ListNode* dummy_node = malloc(sizeof(struct ListNode));
    dummy_node->val = 0;
    dummy_node->next = *head;
    struct ListNode* prev = malloc(sizeof(struct ListNode));
    prev = dummy_node;
    struct ListNode* cur = malloc(sizeof(struct ListNode));
    cur = *head;
    while (cur != NULL)
    {
        if (cur->val == val)
        {
            prev->next = cur->next;
            cur = cur->next;
        }
        else
        {
            prev = cur;
            cur = cur->next;
        }
    }
    return dummy_node->next;
}

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void traversePreorder(struct TreeNode* root, int** myList, int *cnt)
{
    (*myList) = (int*)realloc((*myList), sizeof(int) * (*cnt + 1));
    (* myList)[*cnt] = root->val;
    *cnt = *cnt + 1;
    if (root->left != NULL)
    {
        traversePreorder(root->left, myList, cnt);
    }
    if (root->right != NULL)
    {
        traversePreorder(root->right, myList, cnt);
    }
}

void flatten(struct TreeNode* root) {
    int cnt = 0;
    int* myList = malloc(0);
 
    if (root != NULL)
    {
        traversePreorder(root, &myList, &cnt);
        struct TreeNode* cur = root;
        for (int i = 1;i < cnt;i++)
        {
            cur->left = NULL;
            struct TreeNode* temp = malloc(sizeof(struct TreeNode));
            temp->val = myList[i];
            cur->right = temp;
            cur = cur->right;
        }
        cur->left = NULL;
        cur->right = NULL;
    }
}

void preorderTraverse(struct TreeNode* root) 
{
    if (root->left != NULL)
    {
        preorderTraverse(root->left);
    }
    printf("%d -> ", root->val);
    if (root->right != NULL)
    {
        preorderTraverse(root->right);
    }
}

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void traverseInorder(struct TreeNode *root, int **myList, int *cnt)
{   
    (*myList) = (int*)realloc((*myList), sizeof(int) * (*cnt + 1));
    if (root->left != NULL)
    {
        traverseInorder(root->left, myList, cnt);
    }
    (* myList)[*cnt] = root->val;
    *cnt = *cnt + 1;
    if (root->right != NULL)
    {
        traverseInorder(root->right, myList, cnt);
    }
}

bool isValidBST(struct TreeNode* root) 
{
    int* myList = malloc(0);
    int cnt = 0;
    traverseInorder(root, &myList, &cnt);
    for (int i = 1; i < cnt; i++)
    {
        if (myList[i - 1] >= myList[i])
        {
            return false;
        }
    }
    return true;
}

//left = 0
//right = len(nums) - 1
//start = -1
//
//while left <= right:
//    mid = (left + right) // 2
//    if nums[mid] == target :
//        start = mid
//        right = mid - 1
//    elif nums[mid] > target:
//        right = mid - 1
//    else:
//        left = mid + 1

int* searchRange(int* nums, int numsSize, int target, int* returnSize) 
{
    int left = 0;
    int right = numsSize - 1;
    int start = -1;
    int mid;

    while (left <= right)
    {
        mid = (left + right) / 2;
        if (nums[mid] == target)
        {
            start = mid;
            right = mid - 1;
        }
        else if (nums[mid] > target)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }

    left = 0;
    right = numsSize - 1;
    int end = -1;

    while (left <= right)
    {
        mid = (left + right) / 2;
        if (nums[mid] == target)
        {
            end = mid;
            left = mid + 1;
        }
        else if (nums[mid] > target)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }

    int* res = malloc(sizeof(int) * 2);
    *returnSize = 2;
    res[0] = start;
    res[1] = end;
    return res;
}

int* countingBits(int n, int *resSize)
{
    int* res = malloc(1000);
    int num = n;
    int cnt = 1;
    *resSize = 0;
    while (num > 0)
    {
        if (num % 2 == 1)
        {
            res[*resSize] = cnt;
            *resSize = *resSize + 1;
        }
        num = num / 2;
        cnt = cnt + 1;
    }
    return res;
}

int main()
{
    /* count bits */
    /*
    printf("Hello World");
    int n = 5, returnSize;
    int* res = countBits(n,&returnSize);
    for (int i = 0; i < returnSize; i++) {
        printf("%d", res[i]);
        printf("\n");
    }
    */
    /* removeNthFromEnd */
    /*
    struct ListNode* ln1 = malloc(sizeof(struct ListNode));
    struct ListNode* ln2 = malloc(sizeof(struct ListNode));
    struct ListNode* ln3 = malloc(sizeof(struct ListNode));
    struct ListNode* ln4 = malloc(sizeof(struct ListNode));
    struct ListNode* ln5 = malloc(sizeof(struct ListNode));
    ln1->val = 1;
    ln2->val = 2;
    ln3->val = 3;
    ln4->val = 4;
    ln5->val = 5;
    ln1->next = ln2;
    ln2->next = ln3;
    ln3->next = ln4;
    ln4->next = ln5;
    ln5->next = NULL;

    struct ListNode* res = removeNthFromEnd(ln1, 2);
    while (res != NULL ) {
        printf("%d", res->val);
        printf("\n");
        res = res->next;
    }
    */
    /* insertIntoBST */
    /*
    struct TreeNode* node1 = newNode(4);
    struct TreeNode* node2 = newNode(2);
    struct TreeNode* node3 = newNode(7);
    struct TreeNode* node4 = newNode(1);
    struct TreeNode* node5 = newNode(3);
    node1->left = node2;
    node1->right = node3;
    node2->left = node4;
    node2->right = node5;
    //inorderTraverse(node1);
    //inorderTraverse(insertIntoBST(node1, 5));
    int cnt = 0;
    inorderTraverse(insertIntoBST(node1, 5, &cnt));
    
    int arr[5] = {4, 2, 7, 1, 3};
    struct TreeNode *root = NULL;
    for (int i = 0;i < 5;i++) {
        root = insertIntoBST(root, arr[i], &cnt);
    }
    printf("%d", cnt);
    */
    ///* maxPlanes */
    //int startHeight[5] = {1, 3, 5, 4, 8};
    //int descentRate[5] = {1, 2, 2, 1, 2};
    //int n = sizeof(startHeight) / sizeof(startHeight[0]);
    //int maxNum = maxPlanes(startHeight, descentRate, n);
    /* removeElements */
    //struct ListNode* ln1 = malloc(sizeof(struct ListNode));
    //struct ListNode* ln2 = malloc(sizeof(struct ListNode));
    //struct ListNode* ln3 = malloc(sizeof(struct ListNode));
    //struct ListNode* ln4 = malloc(sizeof(struct ListNode));
    //struct ListNode* ln5 = malloc(sizeof(struct ListNode));
    //struct ListNode* ln6 = malloc(sizeof(struct ListNode));
    //struct ListNode* ln7 = malloc(sizeof(struct ListNode));
    //ln1->val = 1;
    //ln2->val = 2;
    //ln3->val = 6;
    //ln4->val = 3;
    //ln5->val = 4;
    //ln6->val = 5;
    //ln7->val = 6;
    //ln1->next = ln2;
    //ln2->next = ln3;
    //ln3->next = ln4;
    //ln4->next = ln5;
    //ln5->next = ln6;
    //ln6->next = ln7;
    //ln7->next = NULL;
    ////ListNodeTraverse(ln1);
    ////struct LIstNode *head = removeElements(ln1, 6);
    ////ListNodeTraverse(head);
    //struct LIstNode* head = removeElements(&ln1, 6);
    //ListNodeTraverse(head);
    /* C is not a safe language */
    //int myarray[2];
    //printf("%d ", myarray[5]);
    // 
    //int* a = malloc(100);
    //free(a);
    //a[10] = 6;
    /*printf("%d\n", INT_MAX + 1);*/
    ///* flatten */
    //struct TreeNode* tn1 = malloc(sizeof(struct TreeNode));
    //struct TreeNode* tn2 = malloc(sizeof(struct TreeNode));
    //struct TreeNode* tn3 = malloc(sizeof(struct TreeNode));
    //struct TreeNode* tn4 = malloc(sizeof(struct TreeNode));
    //struct TreeNode* tn5 = malloc(sizeof(struct TreeNode));
    //struct TreeNode* tn6 = malloc(sizeof(struct TreeNode));
    //tn1->val = 1;
    //tn2->val = 2;
    //tn3->val = 5;
    //tn4->val = 3;
    //tn5->val = 4;
    //tn6->val = 6;
    //tn1->left = tn2;
    //tn1->right = tn3;
    //tn2->left = tn4;
    //tn2->right = tn5;
    //tn3->left = NULL;
    //tn3->right = tn6;
    //tn4->left = NULL;
    //tn4->right = NULL;
    //tn5->left = NULL;
    //tn5->right = NULL;
    //tn6->left = NULL;
    //tn6->right = NULL;
    //flatten(tn1);
    //preorderTraverse(tn1);
    ///* isValidBST */
    //struct TreeNode* tn1 = malloc(sizeof(struct TreeNode));
    //struct TreeNode* tn2 = malloc(sizeof(struct TreeNode));
    //struct TreeNode* tn3 = malloc(sizeof(struct TreeNode));
    //struct TreeNode* tn4 = malloc(sizeof(struct TreeNode));
    //struct TreeNode* tn5 = malloc(sizeof(struct TreeNode));
    //tn1->val = 4;
    //tn2->val = 2;
    //tn3->val = 7;
    //tn4->val = 1;
    //tn5->val = 3;
    //tn1->left = tn2;
    //tn1->right = tn3;
    //tn2->left = tn4;
    //tn2->right = tn5;
    //tn3->left = NULL;
    //tn3->right = NULL;
    //tn4->left = NULL;
    //tn4->right = NULL;
    //tn5->left = NULL;
    //tn5->right = NULL;

    //printf("%d ", isValidBST(tn1));
    ///* searchRange */
    //int nums[6] = {5, 7, 7, 8, 8, 10};
    //int numsSize = 6;
    //int target = 8;
    //int returnSize, *res;
    //res = searchRange(nums, numsSize, target, &returnSize);
    //printf("[%d, %d]", res[0], res[1]);
    /* countingBits */
    int resSize;
    int* res;
    int n = 10000;
    res = countingBits(n, &resSize);   
    for (int i = 0;i < resSize;i++)
    {
        printf("%d ->", res[i]);
    }
    printf("Bits Counts: %d", resSize);
}


// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
