import settings
from django.core.management import setup_environ
setup_environ(settings)
from viz.models import DataPoint, Friend
from viz.data import diff_data_points



def main():
    print "Test set intersections"
    dp = DataPoint.objects.all()
    
    for i in range(0, 1000):
        print i
        diff_data_points(dp[1], dp[2])


if __name__ == "__main__":
    main()