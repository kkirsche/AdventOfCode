require "bundler/gem_tasks"
require "rake/testtask"

Rake::TestTask.new(:test) do |t|
  require 'simplecov'
  SimpleCov.start do
    add_filter "/lib/adventOfCode/inputs/"
  end
  require 'minitest/autorun'
  require "adventOfCode"
  require "adventOfCode/days/day1_test"
end

task :default => :test
