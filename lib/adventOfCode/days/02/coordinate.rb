module AdventOfCode
  module Day2
    class Coordinate
      attr_accessor :x, :y
      def initialize(x=2, y=2)
        @x = x
        @y = y
      end

      def coordinate
        return [@x, @y]
      end

      def up
        if can_move_up?
          @y -= 1
        end
      end

      def right
        if can_move_right?
          @x += 1
        end
      end

      def down
        if can_move_down?
          @y += 1
        end
      end

      def left
        if can_move_left?
          @x -= 1
        end
      end

      def can_move_up?
        case value
        when 1
          return false
        when 2
          return false
        when 3
          return false
        end

        true
      end

      def can_move_down?
        case value
        when 7
          return false
        when 8
          return false
        when 9
          return false
        end

        true
      end

      def can_move_left?
        case value
        when 1
          return false
        when 4
          return false
        when 7
          return false
        end

        true
      end

      def can_move_right?
        case value
        when 3
          return false
        when 6
          return false
        when 9
          return false
        end

        true
      end

      def value
        case coordinate
        when [1,1]
          return 1
        when [2,1]
          return 2
        when [3,1]
          return 3
        when [1,2]
          return 4
        when [2,2]
          return 5
        when [3,2]
          return 6
        when [1,3]
          return 7
        when [2,3]
          return 8
        when [3,3]
          return 9
        end
      end
    end
  end
end
