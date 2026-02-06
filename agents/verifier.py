class VerifierAgent:

    def verify(self, results):

        if not results:
            return "Execution failed - No results returned"

        for r in results:
            if "error" in str(r).lower():
                return "Execution partially failed"

        return "Execution successful"
