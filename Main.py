import pygame 
import Scripts

class ShowResult:

    def __init__(self, pos, N):
        self.N = N
        self.size = 540/self.N

        self.screen = pygame.display.set_mode((540, 540))
        pygame.display.set_caption('QueensPuzzle')

        self.pos = pos
        self.running = True  

      # Quit
    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # Display Result
    def display(self):
        self.screen.fill('black')
        for i in range(self.N+1):
            pygame.draw.line(self.screen, (255,255,255), (i*self.size, 0), (i*self.size, self.N*self.size))
            pygame.draw.line(self.screen, (255,255,255), (0, i*self.size), (self.N*self.size, i*self.size))
        for p in self.pos:
            pygame.draw.rect(self.screen, (255,255,255), (p[0]*self.size+self.size/4, p[1]*self.size+self.size/4, self.size-self.size/2, self.size-self.size/2))
        pygame.display.flip()

    def run(self):
        while(self.running):
            self.handling_events()
            self.display()
        



N = 12
pos, n = Scripts.MaxQueens(N)
print(f"max pour n={N}: {n}")

pygame.init()

game = ShowResult(pos, N)
game.run()

pygame.quit()

