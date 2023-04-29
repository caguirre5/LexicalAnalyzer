import tools.textHandler as textHandler
import dataStructures.expressionTree as expressionTree
from algorithms.thompsonNFA import ThompsonNFA
from tools.drawAutomaton import getNFA, getDFA
from tools.drawTree import buildGraph
from algorithms.subsetDFA import SubsetConstruction
from tools.simulacion import simulate_afd, simulate_afn
from algorithms.directDFA import construct_afd
from algorithms.minimize import minimize_afd