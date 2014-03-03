package main

import (
	"fmt"
	"strings"
)

func splitOnPunct(r rune) bool {
	return r == '.' || r == '!' || r == '?'
}

func isPunct(r rune) rune {
	if int32(r)&64 == 0 {
		return r
	}
	return -1
}

func main() {
	s := "Who is Dylan Hunt? He is Captain of the Andromeda Ascendant. I don't like him much!"
	fmt.Printf("Test on the string %s\n", s)

	// Python: "Dylan" in s
	fmt.Println("Is 'Dylan' in there?", strings.Contains(s, "Dylan"))

	// Python: s.count("an")
	fmt.Println("Count occurrences of 'an':", strings.Count(s, "an"))

	// Python: s.split()
	fmt.Println("Split the string on whitespace:", strings.Fields(s)[0:3], "...")

	// Python: re.split("[.!?]", s)
	fmt.Println("Split the string on user defined function:", strings.FieldsFunc(s, splitOnPunct), "...")

	// Python: s.startswith("Who")
	fmt.Println("Does it start with 'Who'?", strings.HasPrefix(s, "Who"))

	// Python: s.endswith("Trance")
	fmt.Println("Does it end with 'Trance'?", strings.HasSuffix(s, "Trance"))

	// Python: s.find("Andromeda") == s.index("Andromeda")
	// Also relevant is s.rfind which is equivalent to strings.LastIndex
	fmt.Println("Where does 'Andromeda' occur?", strings.Index(s, "Andromeda"))

	// Python: "|".join(s.split()[:5])
	fmt.Println("Join words together with a pipe:", strings.Join(strings.Fields(s)[0:5], "|"))

	// Python: "".join(x if x.ispunct() else "" for x in s)
	fmt.Println("Return only the punctuation in s: \"" + strings.Map(isPunct, s) + "\"")

	// Python: "Dylan" * 3
	fmt.Println("Dylan times three:", strings.Repeat("Dylan", 3))

	// Python: s.split("a")
	fmt.Println("Split on the letter 'a':", strings.Split(s, "a"))

	// Python: s.title()
	fmt.Println("Titled s:", strings.Title(s))

	// Python: s.lower() and s.upper()
	fmt.Println(strings.ToLower(s), strings.ToUpper(s))

	// Python: s.strip() => strings.TrimSpace(s)
	// Python: s.strip() except you can define it on more than just whitespace
	fmt.Println(strings.Trim(" This is the test   ?", " ?"))
}
