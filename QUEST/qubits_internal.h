# ifndef QUBITS_INTERNAL
# define QUBITS_INTERNAL

/** @file
 * Internal functions used to implement the public facing API in qubits.h. Do not call these functions
 * directly. In general, qubits_env_local.c and qubits_env_mpi.c will implement the public API by choosing
 * the correct function or combination of functions to use from those included here.  
 */

void rotateQubitLocal (MultiQubit multiQubit, const int rotQubit, Complex alpha, Complex beta);

void rotateQubitDistributed (MultiQubit multiQubit, const int rotQubit,
                Complex rot1, Complex rot2,
                ComplexArray stateVecUp,
                ComplexArray stateVecLo,
                ComplexArray stateVecOut);

double findProbabilityOfZeroLocal (MultiQubit multiQubit,
                const int measureQubit);

double findProbabilityOfZeroDistributed (MultiQubit multiQubit,
                const int measureQubit);

int extractBit (const int locationOfBitFromRight, const long long int theEncodedNumber);

void measureInZeroLocal(MultiQubit multiQubit, int measureQubit, double totalProbability);

double measureInZeroDistributedRenorm (MultiQubit multiQubit, const int measureQubit, const double totalProbability);

void measureInZeroDistributedSetZero(MultiQubit multiQubit, const int measureQubit);

double filterOut111 (const int numQubits, const int idQubit1, const int idQubit2, const int idQubit3,
                              double *restrict stateVecReal,
                              double *restrict stateVecImag);

double probOfFilterOut111 (const int numQubits, const int idQubit1, const int idQubit2, const int idQubit3,
                              double *restrict stateVecReal,
                              double *restrict stateVecImag);

# endif
