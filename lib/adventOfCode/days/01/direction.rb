module AdventOfCode
  module Day1
    class Direction
      attr_accessor :turn, :spaces
      def initialize(direction)
        # Get the R or L
        @turn = direction[0,1]
        # Get the number of spaces to move
        @spaces = direction[1,2].to_i
      end

      def take_direction(current_position)
          current_position.turn self

        current_position
      end

      def left?
        return @turn == 'L'
      end

      def right?
        return @turn == 'R'
      end
    end
  end
end
