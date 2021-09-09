#include<stdio.h>
#include <math.h>

int main() {
	int w = 0;
	int h = 0;
	int n = 0;
	scanf("%d %d %d", &w, &h, &n);

	int area_of_rect = w * h * n;

	int square_side = sqrt(w * h * n);
	int answer_found = 0;

	while (!answer_found) {
		int height_count = 1;
		int width_count = 1;

		while (height_count * h <= square_side) {
			height_count += 1;
		}
		while (width_count * w <= square_side) {
			width_count += 1;
		}

		if (n <= width_count + height_count) {
			square_side++;
		}

	}
	printf("%d", square_side);
	return 0;
}
