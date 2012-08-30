import numpy as np
import sys, os

def forced_vibrations(t, I, m, b, f, F):
    """
    Solve a vibrating system problem m*u'' + b*u' + f(u) = F(t)
    with u(0)=I and u'(0)=0, for time values in the array t,
    by a finite difference method. Return u.
    u is an array of the same size as the array F and t.
    """
    dt = t[1] - t[0]           # time step
    N = t.size - 1             # no of time intervals
    u = np.zeros(N+1)

    # Precompute constants
    Cp = b/2*dt + m
    Cm = b/2*dt - m
    m2 = 2*m
    dt2 = dt**2

    u[0] = I
    u[1] = u[0] + (dt**2/(2*m))*(F[0] - f(u[0]))

    for n in range(1, N):
        u[n+1] = (Cm*u[n-1] + m2*u[n] - dt2*(f(u[n]) - F[n]))/Cp
    return u

def acceleration(h, x, v):
    # Compute 2nd-order derivative of h
    d2h = np.zeros(h.size)
    dx = x[1] - x[0]
    for i in range(1, h.size-1, 1):
        d2h[i] = (h[i-1] - 2*h[i] + h[i+1])/dx**2
    # Extraplolate end values from first interior value
    d2h[0] = d2h[1]
    d2h[-1] = d2h[-2]
    a = d2h*v**2
    return a

def solve(url=None, m=60, b=80, k=60, v=5):
    """
    Solve model for verticle vehicle vibrations.

    =========   ==============================================
    variable    description
    =========   ==============================================
    url         either URL of file with excitation force data,
                or name of a local file
    m           mass of system
    b           friction parameter
    k           spring parameter
    v           (constant) velocity of vehicle
    Return      data (list) holding input and output data
                [x, t, [h,a,u], [h,a,u], ...]
    =========   ==============================================
    """
    # Download file (if url is not the name of a local file)
    if url.startswith('http://') or url.startswith('file://'):
        import urllib
        filename = os.path.basename(url)  # strip off path
        urllib.urlretrieve(url, filename)
    else:
        # Check if url is the name of a local file
        filename = url
        if not os.path.isfile(filename):
            print url, 'must be a URL or a filename'
            sys.exit(1)
        # else: ok

    # Load file data into array h_data
    try:
        h_data = np.loadtxt(filename)  # read numpy array from file
    except ValueError:
        print 'Wrong format in file', url
        sys.exit(1)

    x = h_data[0,:]                # 1st column: x coordinates
    h_data = h_data[1:,:]          # other columns: h shapes

    t = x/v                        # time corresponding to x
    dt = t[1] - t[0]
    if dt > 2/np.sqrt(k/float(m)):
        print 'Unstable scheme'

    def f(u):
        return k*u

    data = [x, t]      # key input and output data (arrays)
    for i in range(h_data.shape[0]):
        h = h_data[i,:]            # extract a column
        a = acceleration(h, x, v)

        u = forced_vibrations(t=t, I=0.2, m=m, b=b, f=f, F=-m*a)
        data.append([h, a, u])
    return data

def rms(data):
    """Compute root mean square of displacement."""
    t = data[1]  # (recall: data = [x,t,[h,a,u],[h,a,u],...,])
    u_rms = np.zeros(t.size)
    for h, a, u in data[2:]:
        u_rms += u**2
    u_rms = np.sqrt(u_rms/u_rms.size)
    data.append(u_rms)
    return data

def prepare_input():
    url = 'http://hplbit.bitbucket.org/data/bumpy/bumpy.dat.gz'
    m = 60
    k = 60
    v = 5
    try:
        b = float(sys.argv[1])
    except IndexError:
        b = 80  # default
    return url, m, b, k, v

def command_line_options():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--m', '--mass', type=float,
                        default=60, help='mass of vehicle')
    parser.add_argument('--k', '--spring', type=float,
                        default=60, help='spring parameter')
    parser.add_argument('--b', '--damping', type=float,
                        default=80, help='damping parameter')
    parser.add_argument('--v', '--velocity', type=float,
                        default=5, help='velocity of vehicle')
    url = 'http://hplbit.bitbucket.org/data/bumpy/bumpy.dat.gz'
    parser.add_argument('--roadfile', type=str,
              default=url, help='filename/URL with road data')
    args = parser.parse_args()
    # Extract input parameters
    m = args.m; k = args.k; b = args.b; v = args.v
    url = args.roadfile
    return url, m, b, k, v

if __name__ == '__main__':
    #url, m, b, k, v = prepare_input()
    url, m, b, k, v = command_line_options()

    data = solve(url=url, m=60, b=b, k=60, v=10)
    data = rms(data)

    # Save data list to file
    import cPickle
    outfile = open('bumpy.res', 'w')
    cPickle.dump(data, outfile)
    outfile.close()
