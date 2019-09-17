import sys
import math

class point:
    def __init__( self, x, y, z):
        self.x, self.y, self.z = x, y, z
    
    def distfrom( self, x, y, z ):
        return math.sqrt( (self.x-x)**2 + (self.y-y)**2 + (self.z-z)**2 )
    
    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getz(self):
        return self.z

def main ():
    fn = ""
    if len(sys.argv) != 2:
        print ("usage: ", sys.argv[0], " filename")
        exit(1)
    else:
        fn = sys.argv[1]

    fp = open(fn)
    line  = fp.readline()
    xs, ys, zs = line.split()
    pp = point(float(xs), float(ys), float(zs))
    totdist = 0.0
    for line in fp:
        xs, ys, zs = line.split()

        #print (pp.getx(), pp.gety(), pp.getz())
        ap = point(float(xs), float(ys), float(zs))
        dist = ap.distfrom(pp.getx(), pp.gety(), pp.getz())
        pp = point(ap.getx(), ap.gety(), ap.getz())
        #print (pp.getx(), pp.gety(), pp.getz()) 
        print (dist)

        totdist += dist

    fp.close()

    print ("Total dist: %10.5f "%totdist)


if __name__== "__main__":

    main()

