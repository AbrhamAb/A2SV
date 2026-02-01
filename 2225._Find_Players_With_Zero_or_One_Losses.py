class Solution:
    def findWinners(self, matches):
        losses = {}

        for w, l in matches:
            if w not in losses:
                losses[w] = 0

            if l not in losses:
                losses[l] = 0
            losses[l] += 1

        zero_loss = []
        one_loss = []

        for p in losses:
            if losses[p] == 0:
                zero_loss.append(p)
            elif losses[p] == 1:
                one_loss.append(p)

        zero_loss.sort()
        one_loss.sort()

        return [zero_loss, one_loss]
