if __name__ == "__main__":
    x, y, w, h = map(int, input().split())
    
    shortLenToWidthBoundary = min(x, w - x)
    shortLenToHeightBoundary = min(y, h - y)
    
    print(min(shortLenToWidthBoundary, shortLenToHeightBoundary))
