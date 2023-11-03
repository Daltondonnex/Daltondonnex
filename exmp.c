#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
	int num;
	struct node *ptr;
}ND;

ND *head;
int count=0;

void printing()
{
	ND *temp;
	temp=head;
	printf("\nTHE ELEMENTS OF THE LINKED LIST ARE DISPLAYED BELOW\n");
	while(temp!=NULL)
	{
		printf("%d ",temp->num);
		temp=temp->ptr;
	}
	printf("\n");
}

void insertion()
{
	ND *temp,*value;
	int l,val,c=0;
	printf("\nENTER THE LOCATION TO ENTER NEW NODE(between 0 & %d)=",count);
	scanf("%d",&l);

	if(l>=0 && l<=count)
	{
		printf("ENTER THE VALUE TO BE PUT IN THE NODE=");
		scanf("%d",&val);
		temp=head;
		while((l-1)>c)
		{
			temp=temp->ptr;
			c++;
		}

		value=(ND *)malloc(sizeof(ND));
		if(l==0)
		{
			value->num=val;
			value->ptr=head;
			head=value;
		}
		else
		{
			value->num=val;
			value->ptr=temp->ptr;
			temp->ptr=value;
		}
		count++;
	}
}

void deletion()
{
	ND *temp,*value,*f;
	int l,c=1;
	printf("\nENTER THE NODE NO. TO DELETE(between 1 & %d)=",count);
	scanf("%d",&l);

	if(l>=1 && l<=count)
	{
		temp=head;
		while((l-1)>c)
		{
			temp=temp->ptr;
			c++;
		}

		if(l==1)
		{
			f=head;
			head=head->ptr;
		}
		else
		{
			f=temp->ptr;
			temp->ptr=temp->ptr->ptr;
		}
		free(f);
		count--;
	}
}

int main(void)
{
	int choice=0;
	head=NULL;
	printf("THIS IS A PROGRAM TO INSERT/DELETE/COUNT/PRINT NUMBERS OF A LINEAR LINKED LIST\n");

	while(choice!=5)
	{
      printf("\nENTER 1 TO COUNT NO. OF NODES\n");
		printf("ENTER 2 TO INSERT NODE\n");
		printf("ENTER 3 TO DELETE NODE\n");
		printf("ENTER 4 TO PRINT ENTIRE LINKED LIST\n");
		printf("ENTER 5 TO EXIT THE LINKED LIST\n");
		printf("ENTER HERE=");
		scanf("%d",&choice);

		switch(choice)
		{
			case 1:
					printf("\nTHERE ARE %d NODES\n",count);
					break;

			case 2:
					insertion();
					printf("THERE ARE %d NODE/NODES NOW",count);
					printing();
					break;

			case 3:
					 if(count==0)
						printf("\nTHE LIST IS EMPTY, INSERT NUMBERS FIRST\n");
					 else
					 {
						deletion();
						printf("THERE ARE %d NODES",count);
						printing();
					 }
					 break;

			case 4:
					 if(count==0)
						printf("\nTHE LIST IS EMPTY, INSERT NUMBERS FIRST\n");
					 else
						printing();
					 break;

			default: break;
		}
	}
	if(choice==5)
	 exit(0);
	return 0;
}

