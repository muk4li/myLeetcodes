def meineLoesung(nums1, nums2):
    fused = sorted(nums1 + nums2)

    n = len(fused)

    if n % 2 == 1:
        median = fused[n // 2]
    else:
        a = fused[n // 2 - 1]
        b = fused[n // 2]
        median = (a + b) / 2

    return median


def optimaleLoesung(nums1, nums2):
    """
    Meine Erklärung zur optimalen Lösung. Wir "mergen" nur gedanklich (=> bessere Performance/Speiche, es war auch gefordert unter log 0 mn whatever zu bleiben).
    Gedanklich gemerged wird, indem man erstmal die kürzere Liste identifiziert.
    An der kürzeren Liste erstmal an der Hälfte den Schnittpunkt setzen, links gehört zur LINKEN Hälfte der gedanklich-gemergted Liste,
    rechts ist die RECHTE Hälfte. Wir Schneiden bei der zweiten/längeren Liste soweit ab, bis LINKS und RECHTS (der gemergten) ~gleich viele Elemente haben.
    Jetzt ist die Frage sind jeweils die höchsten Zahlen der LINKEN Hälfte kleiner als die kleinsten Zahlen der RECHTEN. Sobald
    das erreicht ist und beide Hälften ~gleich groß bleiben, kennen wir den perfekten Schnitt und bei ungerade ist es exakt die
    höchste Zahl der LINKEN Hälfte. Bei Geraden ist es höchste LINKS,kleine RECHTS geteilt 2 => Median.
    """
    # Immer auf der kürzeren Liste binär suchen
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2

    left, right = 0, m

    while left <= right:
        i = (left + right) // 2
        j = half - i

        nums1_left = nums1[i - 1] if i > 0 else float("-inf")
        nums1_right = nums1[i] if i < m else float("inf")

        nums2_left = nums2[j - 1] if j > 0 else float("-inf")
        nums2_right = nums2[j] if j < n else float("inf")

        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            # Richtige Aufteilung gefunden
            if total % 2 == 1:
                return float(max(nums1_left, nums2_left))
            else:
                return (
                    max(nums1_left, nums2_left)
                    + min(nums1_right, nums2_right)
                ) / 2

        elif nums1_left > nums2_right:
            # Zu viele Elemente aus nums1 links
            right = i - 1
        else:
            # Zu wenige Elemente aus nums1 links
            left = i + 1


def main():
    nums1 = [1, 3]
    nums2 = [2]

    print("---- Meine Lösung ---")
    print(meineLoesung(nums1, nums2))

    print("--- optimale Lösung ---")
    print(optimaleLoesung(nums1, nums2))


if __name__ == "__main__":
    main()