import pygame
pygame.init()

size = (600, 600)

screen = pygame.display.set_mode(size)

image_file = pygame.image.load("c2f2.jpg")

image = pygame.transform.scale(image_file, (600, 600))

print("Hello")


def maxRed():

	for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))

				r = 255
				g = color[1]
				b = color[2]

				screen.set_at((x, y), (r, g, b))

def maxGreen():

	for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))
				r = color[0]
				g = 255
				b = color[2]

				screen.set_at((x, y), (r, g, b))

def maxBlue():

	for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))

				r = color[0]
				g = color[1]
				b = 255

				screen.set_at((x, y), (r, g, b))



def maxPurple():

	for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))

				r = 255
				g = color[1]
				b = 255

				screen.set_at((x, y), (r, g, b))


def maxYellow():

	for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))


				r = 255
				g = 255
				b = color[2]

				screen.set_at((x, y), (r, g, b))

def maxCyan():

	for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))

				r = color[0]
				g = 255
				b = 255

				screen.set_at((x, y), (r, g, b))

def purpleAura():

	for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))

				r = 138
				g = color[1]
				b = 218

				screen.set_at((x, y), (r, g, b))


def brighten():


		for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))
				r = color[0] + 15
				g = color[1] + 15
				b = color[2] + 15

				if r > 255:
					r = 255
				if g > 255:
					g = 255
				if b > 255:
					b = 255

				screen.set_at((x, y), (r, g, b))

def darken():

		for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x,y))
				r = color[0] - 15
				g = color[1] - 15
				b = color[2] - 15

				if r < 0:
					r = 0
				if g < 0:
					g = 0
				if b < 0:
					b = 0
				screen.set_at((x, y), (r, g, b))

def rmGreen():

	for x in range(0, 600):
		for y in range(0,600):
			color = screen.get_at((x, y))

			r = color[0]
			g = 0
			b = color[2]

			screen.set_at((x, y), (r, g, b))




def rmRed():

		for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))

				r = 0
				g = color[1]
				b = color[2]

				screen.set_at((x, y), (r, g, b))



def rmBlue():

	for x in range(0, 600):
		for y in range(0, 600):
			color = screen.get_at((x, y))

			r = color[0]
			g = color[1]
			b = 0

			screen.set_at((x, y), (r, g, b))

def negate():

	for x in range(0, 600):
		for y in range(0, 600):
			color = screen.get_at((x, y))

			r = 255 - color[0]
			g = 255 - color[1]
			b = 255 - color[2]

			screen.set_at((x, y), (r, g, b))


def intensify():
	for x in range(0, 600):
		for y in range(0, 600):
			color = screen.get_at((x, y))

			r = color[0]
			g = color[1]
			b = color[2]

			if r > 255 / 2:
				r = 255
			else:
				r = 0

			if g > 255 / 2:
				g = 255
			else:
				g = 0
			if b > 255 / 2:
				b = 255
			else:
				b = 0

			screen.set_at((x, y), (r, g, b))


def greyscale():


	for x in range(0,600):
		for y in range(0, 600):
			color = screen.get_at((x,y))

			r = color[0]
			g = color[1]
			b = color[2]

			average = (r+g+b) / 3
			screen.set_at((x, y), (average, average, average))

def two_tone():

	for x in range(0,600):
		for y in range(0, 600):
			color = screen.get_at((x,y))

			r = color[0]
			g = color[1]
			b = color[2]

			brightness = r + g +b

			if brightness > (255 * 3)/2.0:
				screen.set_at((x, y), (255, 255, 255))

			else:
				screen.set_at((x,y), (0, 0, 0))

def four_tone():

	for x in range(0,600):
		for y in range(0, 600):
			color = screen.get_at((x,y))

			max = 255 * 3

			r = color[0]
			g = color[1]
			b = color[2]

		brightness = r + g + b

		if brightness > (3/4) * max:
			screen.set_at((x, y), (240, 240, 120))

		elif brightness > (2/4) * max:

			screen.set_at((x,y), (240, 30, 30))

		elif brightness > (1/4) * max:
			screen.set_at((x,y), (15, 150, 15))

		else:
			screen.set_at((x, y), (15, 15, 80))

def sepia():

	for x in range(0,600):
		for y in range(0, 600):
			color = screen.get_at((x,y))

			r = color[0]
			g = color[1]
			b = color[2]


			final_r = 0.393 * r + 0.769 * g + 0.189 * b

			final_g = 0.349 * r + 0.686 * g + 0.168 * b

			final_b = 0.272 * r + .534 * g + 0.131 * b

			if final_r > 255:
				final_r = 255

			if final_g > 255:
				final_g = 255

			if final_b > 255:
				final_b = 255


			screen.set_at((x, y),(final_r, final_g, final_b ))


def harry_potter_mode():

	for x in range(0,600):
		for y in range(0, 600):
			color = screen.get_at((x,y))

			r = color[0]
			g = color[1]
			b = color[2]


			final_r = 0.293 * r + 0.669 * g + 0.089 * b

			final_g = 0.449 * r + 0.887 * g + 0.234 * b

			final_b = 0.172 * r + .434 * g + 0.031 * b

			if final_r > 255:
				final_r = 255

			if final_g > 255:
				final_g = 255

			if final_b > 255:
				final_b = 255


			screen.set_at((x, y),(final_r, final_g, final_b ))




def verticalStripes():

	for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))

				if x % 2 == 0:

					r = color[0]
					g = color[1]
					b = color[2]
					screen.set_at((x, y), (r, g, b))

				else:
					screen.set_at((x, y), (0, 255, 0))

def horizontalStripes():

	for x in range(0, 600):
			for y in range(0, 600):
				color = screen.get_at((x, y))

				if y % 2 == 0:

					r = color[0]
					g = color[1]
					b = color[2]
					screen.set_at((x, y), (r, g, b))

				else:
					screen.set_at((x, y), (0, 255, 0))



def mirrorY():

	for x in range(0, 300):
		for y in range(0,600):
			color = screen.get_at((x, y))

			r = color[0]
			g = color[1]
			b = color[2]
			screen.set_at((x, y), (r, g, b))
			screen.set_at((600 - x, y), (r, g, b))


def mirrorX():

	for x in range(0, 600):
		for y in range(0,300):
			color = screen.get_at((x, y))

			r = color[0]
			g = color[1]
			b = color[2]
			screen.set_at((x, y), (r, g, b))
			screen.set_at((x, 600 - y), (r, g, b))




running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_l:
				screen.blit(image, image.get_rect())

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_b:
				brighten()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				darken()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				rmRed()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				rmGreen()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_e:
				rmBlue()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				pygame.image.save(screen, "c2f.png")

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_n:
				negate()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_i:
				intensify()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_g:
				greyscale()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_t:
				two_tone()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_f:
				four_tone()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				sepia()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_z:
				maxRed()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				maxGreen()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c:
				maxBlue()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				maxPurple()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_y:
				maxYellow()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_o:
				maxCyan()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_6:
				purpleAura()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_9:
				harry_potter_mode()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_4:
				verticalStripes()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_5:
				horizontalStripes()

		if event.type == pygame.KEYDOWN:
			if event.key== pygame.K_7:
				mirrorY()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_u:
				mirrorX()


	pygame.display.flip()

