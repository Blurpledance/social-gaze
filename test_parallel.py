from psychopy import parallel
#parallel.setPortAddress(0XD020)
port = parallel.ParallelPort(address=0XD020)
print port.PORT
port.setData(0)
