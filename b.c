#include<stdio.h>
#include<malloc.h>
//#define NULL 0
#define O1 sizeof(struct job)
#define O2 sizeof(struct rest)
#define O3 sizeof(struct use)
int SUM = 100;
int FirstAddress = 1;
char buffer[200];

struct job
{
	int name;
	int size;
	int ad;
};
struct rest
{
	int size;
	int ad;
	struct rest* next;
};
struct use
{
	int name;
	int size;
	int ad;
	struct use* next;
};

struct job* CreateJob(void)
{
	struct job* p;
	p = (struct job*)malloc(O1);
	printf("Enter name(int): ");
	if (fgets(buffer, sizeof(buffer), stdin))
	{
		sscanf_s(buffer, "%d", &p->name, (unsigned int)sizeof(p->name));
		printf("Enter size: ");
		if (fgets(buffer, sizeof(buffer), stdin))
		{
			sscanf_s(buffer, "%d", &p->size,(unsigned int)sizeof(p->size));
			return (p);
		}
	}
	return NULL;
}// 创建作业

/*
Init a LinkList of rest space which has a head node
*/
struct rest* InitRestLinkList(void)
{
	struct rest* head;
	struct rest* p1;
	p1 = (struct rest*)malloc(O2);
	p1->size = SUM;
	p1->ad = FirstAddress;
	p1->next = NULL;
	head = p1;
	return (head);
}

/*
Init a LinkList of rest space which NOT has a head node
*/
struct use* InitUseLinkList(void)
{
	struct use* head;
	head = NULL;
	return(head);
}

struct rest* FFAllocate(struct rest* resthead, struct job* pjob)//首次适应算法 
{
	struct rest* p0, * p1;
	struct job* a;
	a = pjob;
	p0 = resthead;

	
	return(resthead);
}

struct rest* BFAllocate(struct rest* head, struct job* p)//最佳适应算法 
{
	struct rest* p0, * p1;
	struct job* a;
	a = p;
	p0 = head;
	//在此补充分配算法逻辑

	return(head);
}

struct rest* WFAllocate(struct rest* head, struct job* p)//最坏适应算法 
{
	struct rest* p0, * p1;
	struct job* a;
	a = p;
	p0 = head;
	//在此补充分配算法逻辑

	return(head);
}

/*
Link pjob to the last one in use linklist
*/
struct use* UpdateUse(struct use* usehead, struct job* pjob)
{
	struct use* p0, * pjobNew, * p2, * p3, * p4;
	struct job* a;
	a = pjob;
	p0 = (struct use*)malloc(O3);
	pjobNew = (struct use*)malloc(O3);
	if (usehead == NULL)
	{
		p0->name = a->name;
		p0->size = a->size;
		p0->ad = SUM;
		p0->next = NULL;
		usehead = p0;
	}
	else
	{
		pjobNew->name = a->name;
		pjobNew->size = a->size;
		pjobNew->ad = a->ad;
		p2 = usehead;
		while (p2->next != NULL)
		{
			p2 = p2->next;
		}
		p2->next = pjobNew;
		pjobNew->next = NULL;
	}
	return(usehead);
}

/*
Delete Job in use linklist
*/
struct use* DeleteJob(struct use* usehead, struct job* p)
{
	struct job* pjob;
	struct use* cur, * pre;
	cur = usehead;
	pjob = p;
	while ((pjob->name != cur->name) && (cur->next != NULL))
	{
		pre = cur;
		cur = cur->next;

	}
	if (pjob->name == cur->name)
	{
		if (cur == usehead)
			usehead = cur->next;
		else
			pre->next = cur->next;
		free(cur); 
	}
	return (usehead);
}

struct job* GetJob(struct use* usehead)
{
	struct job* p1;
	struct use* p2;
	int num;
	p1 = (struct job*)malloc(O1);
	printf("Enter job name you want to remove: ");
	if (fgets(buffer, sizeof(buffer), stdin))
	{
		sscanf_s(buffer, "%d", &num, (unsigned int)sizeof(num));
	}
	p2 = usehead;
	while ((num != p2->name) && (p2->next != NULL))
	{
		p2 = p2->next;
	}
	if (num == p2->name)
	{
		p1->name = p2->name;
		p1->size = p2->size;
		p1->ad = p2->ad;
	}
	return(p1);
}

/*
Update rest linklist according to the location of job removed
*/
struct rest* UpdateRest(struct job* p, struct rest* resthead)
{
	struct rest* cur, * pre, * pjobNew;
	struct job* pjob;
	pjob = p;
	cur = resthead;
	pjobNew = (struct rest*)malloc(O2);
	pjobNew->size = pjob->size;
	pjobNew->ad = pjob->ad;
	if (!resthead)
	{

	}
	while ((cur->ad < pjob->ad) && (cur->next != NULL))
	{
		pre = cur;
		cur = cur->next;
	}
	if (cur->ad > pjob->ad) // there are rest blocks after pjob
	{
		if (resthead == cur) //no pre rest block
		{
			if ((cur->ad - pjobNew->ad) == (pjobNew->size)) // job is in front of cur closely
			{
				cur->ad = pjobNew->ad;
				cur->size = pjobNew->size + cur->size;
			}
			else // job is in front of cur but not closely
			{
				resthead = pjobNew;
				pjobNew->next = cur;
			}
		}
		else // pre rest block
		{
			if ((cur->ad - pjobNew->ad) == (pjobNew->size)) // job is in front of cur rest block closely
			{
				cur->ad = pjobNew->ad;
				cur->size = pjobNew->size + cur->size;
				if ((pjobNew->ad - pre->ad) == (pre->size))// job is behind pre rest block closely
				{
					pre->size = cur->size + pre->size; pre->next = cur->next;
				}
				else // job is behind pre but not closely
				{
					pre->next = cur;
				}
			}
			else 
			{
				if ((pjobNew->ad - pre->ad) == (pre->size))
				{
					pre->size = pre->size + pjobNew->size;
				}
				else
				{
					pjobNew->next = cur;
					pre->next = pjobNew;
				}
			}
		}
	}
	else // pjob is the last one in space
	{
		if ((pjobNew->ad - cur->ad) == (cur->size)) //pjob is behind cur closely
		{
			cur->size = cur->size + pjobNew->size;
		}
		else
		{
			cur->next = pjobNew;
			pjobNew->next = NULL;
		}
	}
	return(resthead);
}

void structPrint(struct rest* h1, struct use* h2)
{
	struct rest* m1;
	struct use* n1;
	m1 = h1;
	n1 = h2;
	if (m1 == NULL)
	{
		printf("空闲表为空!\n");
	}
	else
	{
		while (m1 != NULL)
		{
			printf("空闲单元地址为%d,其大小为%d\n", m1->ad, m1->size);
			m1 = m1->next;
		}
	}
	if (n1 == NULL)
	{
		printf("已分配表为空!\n");
	}
	else
	{
		while (n1 != NULL)
		{
			printf("已分配单元地址为%d,其大小为%d,其名称为%d\n", n1->ad, n1->size, n1->name);
			n1 = n1->next;
		}
	}
}


void FF(void)
{
	struct rest* prest;
	struct use* puse;
	struct job* pjob, * q;
	int y = 1;
	int n = 0;
	int a = 1;
	int c;
	prest = InitRestLinkList();
	puse = InitUseLinkList();
	printf("初始情况为:\n");
	structPrint(prest, puse);
	while (a == y)
	{
		printf("Enter operation id 1-init job; 2-remove job; 3-end : ");
		if (fgets(buffer, sizeof(buffer), stdin))
		{
			sscanf_s(buffer, "%d", &c, (unsigned int)sizeof(c));
		}
		switch (c)
		{
		case 1:
			pjob = CreateJob();
			prest = FFAllocate(prest, pjob);
			puse = UpdateUse(puse, pjob);
			structPrint(prest, puse); break;
		case 2:
			q = GetJob(puse);
			puse = DeleteJob(puse, q);
			//puse = UpdateUse(puse, q);
			prest = UpdateRest(q, prest);
			structPrint(prest, puse); break;
		case 3:
			y = 0; break;
		}
	}
}

void BF(void)
{
	struct rest* p1;
	struct use* p2;
	struct job* p, * q;
	int y = 1;
	int n = 0;
	int a = 1;
	int c;
	p1 = InitRestLinkList();
	p2 = InitUseLinkList();
	printf("初始情况为:\n");
	structPrint(p1, p2);
	while (a == y)
	{
		printf("Enter operation id 1-init job; 2-remove job; 3-end : ");
		if (fgets(buffer, sizeof(buffer), stdin))
		{
			sscanf_s(buffer, "%d", &c, (unsigned int)sizeof(c));
		}
		switch (c)
		{
		case 1:
			p = CreateJob();
			p1 = BFAllocate(p1, p);
			p2 = UpdateUse(p2, p);
			structPrint(p1, p2); break;
		case 2:
			q = GetJob(p2);
			p2 = DeleteJob(p2, q);
			p1 = UpdateRest(q, p1);
			structPrint(p1, p2); break;
		case 3:
			y = 0; break;
		}
	}
}

void WF(void)
{
	struct rest* p1;
	struct use* p2;
	struct job* p, * q;
	int y = 1;
	int n = 0;
	int a = 1;
	int c;
	p1 = InitRestLinkList();
	p2 = InitUseLinkList();
	printf("初始情况为:\n");
	structPrint(p1, p2);
	while (a == y)
	{
		printf("Enter operation id 1-init job; 2-remove job; 3-end : ");
		if (fgets(buffer, sizeof(buffer), stdin))
		{
			sscanf_s(buffer, "%d", &c, (unsigned int)sizeof(c));
		}
		switch (c)
		{
		case 1:
			p = CreateJob();
			p1 = WFAllocate(p1, p);
			p2 = UpdateUse(p2, p);
			structPrint(p1, p2); break;
		case 2:
			q = GetJob(p2);
			p2 = DeleteJob(p2, q);
			p1 = UpdateRest(q, p1);
			structPrint(p1, p2); break;
		case 3:
			y = 0; break;
		}
	}
}

int main()
{
	printf("先进先出算法的实现\n");
	FF();
	printf("最佳适应算法 \n");
	BF();
	printf("最坏适应算法 \n");
	WF();
	return 0;
