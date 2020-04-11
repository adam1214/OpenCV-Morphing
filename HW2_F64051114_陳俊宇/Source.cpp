#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <stdio.h>

using namespace cv;

void main()
{
	Mat img = imread("women.jpg");
	namedWindow("Display image", WINDOW_AUTOSIZE);
	imshow("Display image", img);
	while (waitKey() != 27);
}
