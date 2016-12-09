module AdventOfCode
  module Day2
    class Challenge
      def initialize(filename)
        set_contents filename
      end

      def run_part_1
        @code = Code.new
        @keypad = Keypad.new
        passcode_directions = @contents.split("\n")

        passcode_directions.each do |directions|
          directions.each_char do |move|
            case move
            when 'U'
              @keypad.up
            when 'R'
              @keypad.right
            when 'D'
              @keypad.down
            when 'L'
              @keypad.left
            end
          end
          @code.next @keypad.code
        end

        @code.value
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
