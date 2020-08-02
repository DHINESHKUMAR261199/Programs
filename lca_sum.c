#include<stdio.h>
#include<stdlib.h>
struct node{
	int d;
	struct node *l,*r;
};
int res=0;
struct node*  ins(int val)
{
	struct node* nn=(struct node *)malloc(sizeof(struct node));
	nn->d=val;
	nn->l=nn->r=NULL;
	return nn;
}

struct node* insert(int a[],struct node* root,int i,int n)
{
	if(i<n)
	{
		struct node* t=ins(a[i]);
		root=t;
		root->l=insert(a,root->l,2*i+1,n);
		root->r=insert(a,root->r,2*i+2,n);
	}
	return root;
}

struct node* LCA(struct node* root, int v1, int v2)
{
    if(root == NULL)
        return NULL;
    if(root->d == v1 || root->d == v2)
        return root;
    else
    {
        struct node *left = LCA(root->l,v1,v2);
        struct node *right = LCA(root->r,v1,v2);
        if(left && right)
            return root;
        if(left)
            return left;
        else
            return right;
    }
}

void calcSum(struct node* root,int lca) 
{ 
    if (root == NULL) 
        return; 
    if (root->d == lca) 
    { 
        res=0;
        if (root->l) 
            res += root->l->d; 
        if (root->r) 
            res += root->r->d; 
    } 
    calcSum(root->l,lca); 
    calcSum(root->r,lca); 
} 
  


main()
{
	int t,z;
	scanf("%d",&t);
	for(z=0;z<t;z++)
	{
		int n,i;
		scanf("%d",&n);
		int a[n];
		for(i=0;i<n;i++)
		    scanf("%d",&a[i]);
		int v1,v2;
		scanf("%d%d",&v1,&v2);
		struct node* root=insert(a,root,0,n);
		int lca=LCA(root,v1,v2)->d;
		printf("   %d    ",lca);
		calcSum(root,lca);
		printf("   %d    ",res);
		printf("%d",res-lca);
	}
}
