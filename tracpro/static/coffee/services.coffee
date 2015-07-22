services = angular.module('trac.services', []);

#=====================================================================
# Date utilities
#=====================================================================
parse_iso8601 = (str) ->
  if str then new Date(Date.parse str) else null

format_iso8601 = (date) ->
  # TODO provide backup when browser doesn't support toISOString
  if date then date.toISOString() else null

#=====================================================================
# Poll service
#=====================================================================
services.factory 'PollService', ['$http', ($http) ->
  new class PollService

    #=====================================================================
    # Fetches latest poll pollruns
    #=====================================================================
    fetchLatestPollRuns: (callback) ->
      $http.get('/pollrun/latest/')
      .success (data) =>
        for pollrun in data.results
          # parse datetime string
          pollrun.conducted_on = parse_iso8601 pollrun.conducted_on

        callback(data.results)

    #=====================================================================
    # Fetches most active regions
    #=====================================================================
    fetchActiveRegions: (callback) ->
      $http.get('/region/most_active/')
      .success (data) =>
        callback(data.results)

    #=====================================================================
    # Fetches most active groups
    #=====================================================================
    fetchActiveGroups: (callback) ->
      $http.get('/group/most_active/')
      .success (data) =>
        callback(data.results)
]
