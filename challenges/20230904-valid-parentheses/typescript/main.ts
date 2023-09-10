import { assertEquals } from "https://deno.land/std@0.201.0/assert/mod.ts";
// https://leetcode.com/problems/valid-parentheses/

// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. Must also accept incepted parentheses like "({})". It must always close the last opened bracket. Must match the entire string.

// Best Runtime: 50ms 94.15%
// Best Memory: 44.90 MB beats 24,45% (Funny that using regex is slower but uses a lot less memory)

function isValid(s: string): boolean {

  if (s.length % 2 != 0) {
    return false;
  }

  const stack: string[] = [];
  const bracketPairs = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (Object.keys(bracketPairs).includes(char)) {
      stack.push(char);
    } else if (Object.values(bracketPairs).includes(char)) {
      const lastBracket = stack.pop();
      if (!lastBracket || char !== bracketPairs[lastBracket]) {
        return false;
      }
    }
  }

  return stack.length === 0;
};


Deno.test("test simple tests", () => {
  const result1 = isValid("()");
  assertEquals(result1, true);

});

Deno.test("test invalid  ]", () => {
  const result1 = isValid("]");
  assertEquals(result1, false);
  
  const result2 = isValid("())");
  assertEquals(result2, false);

});

const result1 = isValid("]");