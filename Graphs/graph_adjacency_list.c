#include <stdio.h>
#define MAXV 1000

typedef struct
{
    int y;
    int weight;
    struct edgenode *next;
} edgenode;

typedef struct
{
    edgenode *edges[MAXV + 1];
    int degree[MAXV + 1];
    int nvertices;
    int nedges;
    int directed;
} graph;

initialize_graph(graph *g, int directed)
{
    int i;

    g->nvertices = 0;
    g->nedges = 0;
    g->directed = directed;
}