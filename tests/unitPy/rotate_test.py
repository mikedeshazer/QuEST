from QuESTFunc import *
from QuESTCore import *
import math

def run_tests():
    testRot()

def testRot():

    numQubits=10
    rotQubit = 0

    angs = [1.2,-2.4,0.3]

    alpha = Complex(math.cos(angs[0]) * math.cos(angs[1]),
                    math.cos(angs[0]) * math.sin(angs[1]) )
    beta  = Complex(math.sin(angs[0]) * math.cos(angs[2]),
                    math.sin(angs[0]) * math.sin(angs[2]) )

    mq = createQureg(numQubits, env)
    mqVerif = createQureg(numQubits, env)

    initStateDebug(mq)
    initStateDebug(mqVerif)
    for i in range(numQubits):
        rotQubit=i
        compactUnitary(mq, rotQubit, alpha, beta)
    
    # note -- this is only checking if the state changed at all due to rotation,
    # not that it changed correctly
    testResults.validate(not testResults.compareStates(mq, mqVerif),
                         'Check state rotated')

    # Rotate back the other way and check we arrive back at the initial state
    # (conjugate transpose of the unitary)
    alpha.imag *= -1
    beta.real  *= -1
    beta.imag  *= -1

    # (order of qubits operated upon doesn't matter)
    for i in range(numQubits):
        rotQubit=i
        compactUnitary(mq, rotQubit, alpha, beta)

    # unitaries are relatively imprecise (10* needed for single precision)
    testResults.validate( testResults.compareStates(mq, mqVerif,
                                                    10*testResults.tolerance),
                          'Check back rotation')

    destroyQureg(mq, env)
    destroyQureg(mqVerif, env)

    # check for normalisation
    numQubits=25
    mq = createQureg(numQubits, env)
    
    initPlusState(mq)
    for i in range(numQubits):
        rotQubit=i
        compactUnitary(mq, rotQubit, alpha, beta)
    
    outcome = calcTotalProb(mq);    
    testResults.validate( testResults.compareReals(1.0, outcome),
                          'Check normalisation')
    destroyQureg(mq, env)


    