module AdventOfCode
  module Day2
    class Keypad
      def initialize(starting_position = {x: 2, y: 2})
        @keypad_size = {
          x: {
            max: 3,
            min: 1
          },
          y: {
            max: 3,
            min: 1
          }
        }
        @coordinate = Coordinate.new starting_position[:x], starting_position[:y]
      end

      def code
        @coordinate.value
      end

      def up
        @coordinate.up
      end

      def right
        @coordinate.right
      end

      def down
        @coordinate.down
      end

      def left
        @coordinate.left
      end

      private
      def input_path(filename)
        File.join(File.expand_path('..', File.expand_path('..', File.dirname(File.expand_path(__FILE__)))), "inputs/day2/#{filename}")
      end

      def set_contents(filename)
        # Get instructions
        file = File.open input_path(filename)
        @contents = file.read
      end
    end
  end
end
