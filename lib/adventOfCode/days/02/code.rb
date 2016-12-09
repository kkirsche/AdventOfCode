module AdventOfCode
  module Day2
    class Code
      def initialize
        @code = []
      end

      def next(number)
        @code << number
      end

      def value
        @code.join('')
      end
    end
  end
end
