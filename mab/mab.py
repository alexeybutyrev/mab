import pickle
import codecs


class MAB:
    """
    Mulitarm Bandint base Class

    ...

    Attributes:
    ----------

    counts : list[int]
        number of times event happend for each arm

    values : list[float]
        total rewards for each arm

    n_arms : int
        number of arms

    version_ids: list
        list of version_ids

    Methods:
    -----------
    reset()
        resets MAB to initial state

    select_arm()
        select index of arm to chose next (the core of the algorithm)

    select_version()
        return version_id for the selected arm (same as select_arm but with version id as output)

    update(chosen_arm, reward)
        updated chosen arm with the received reward

    pickle()
        return pickled self as encoded string

    """

    def __init__(
        self, counts=None, values=None, n_arms=None, version_ids=None, active_arms=None,
    ):
        """
        Args:
            counts (list[int]): number of times event happend for each arm.
                                Defaults to [0] * n_arms
            values (list[float]): total rewards for each arm
                                Defaults to [0.0] * n_arms
            n_arms (int): Number of arms. Defaults to len(counts)
            version_ids (list of strings): List with version ids to return
            active_arms (set): set of indexes of active arms
        """
        if counts is None:
            # set up with zeroes if not defined
            assert n_arms is not None
            counts = [0] * n_arms
            values = [0.0] * n_arms
        else:
            if n_arms is not None:
                assert n_arms == len(counts)

        self.n_arms = len(counts)
        self.counts = counts  # number of counts chose for each arm
        self.values = values  # success rate for each arm

        # we need save start values for reset calls
        self.__init_counts = counts[:]
        self.__init_values = values[:]

        if version_ids is None:
            self.version_ids = list(map(str, range(self.n_arms)))
        else:
            self.version_ids = version_ids
            assert type(version_ids) == list

        self.__version_to_index = {v: i for i, v in enumerate(self.version_ids)}

        if active_arms is None:
            active_arms = set(range(self.n_arms))

        self.active_arms = active_arms

    def __str__(self):
        return str(self.__class__.__name__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __iter__(self):
        # iterator in order to convert the model into dict (https://stackoverflow.com/questions/61517/python-dictionary-from-an-objects-fields)
        for x, y in self.__dict__.items():
            if not x.startswith("_"):
                yield x, y

    def to_dict(self):
        """ Return MAB as a dictionary
            to restore the object later

        Returns:
            [dict]: dictionary with the fields name and params
        """
        return {"name": self.__class__.__name__, "params": dict(self)}

    def reset(self):
        """Reset MAB. Sets counts and values to the inital state"""

        self.counts = self.__init_counts[:]
        self.values = self.__init_values[:]

    def select_arm(self):
        """Select Arm of MAB:
        returns index of the arms
        must be chosed by algorythm
        """
        pass

    def select_version(self):
        """ return version_id for selected arm
        """
        return self.select_version[self.select_arm()]

    def update(self, chosen_arm, reward):
        """Update chosen arm

        Args:
            chosen_arm (int or str): arm index or version_id
            reward (float): reward
        """
        if type(chosen_arm) == str:
            chosen_arm = self.__version_to_index[chosen_arm]

        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        self.values[chosen_arm] = ((n - 1) / n) * self.values[chosen_arm] + reward / n

    def compare_to_ab(self):
        """Compare collected rewards agains potential AB test ones
           ## TODO run it on fly when we're updating rewards now the operation in O(narms) the other case would be O(1)
        """

        # AB_rewards 2 cases n/2 * (rewards_1/counts_1) + n/2 * (rewards_2/counts_2) which is euqal
        # AB_rewards = n/2 (rewards_1/counts_1 + rewards_2/counts_2 )
        # rewards_1/counts_1 == values_1
        # below is the caclulation of the second multiplier
        ab_rewards = 0
        total_rewards = 0
        for i in range(self.n_arms):
            ab_rewards += self.values[i]
            total_rewards += self.values[i] * self.counts[i]

        # multiply result // n_arms. // operator to make it as integer for vis purposes
        ab_rewards *= sum(self.counts) // self.n_arms

        return total_rewards - ab_rewards

    def pickle(self):
        """ Pickle itself into a string

        Returns:
            [str]: pickled encoded file
        """

        return codecs.encode(pickle.dumps(self), "base64").decode()

    def add_version(self, version_id=None, is_active=True):
        """ Add version to MAB
            Same as add ARM
        Args:
            version_id (str, optional): version_id of the MAB arm. Defaults to None.
        """
        self.add_arm(version_id, is_active)

    def add_arm(self, version_id=None, is_active=True):
        """ Add ARM to MAB
            
            Args:
            version_id (str, optional): version_id of the MAB arm. Defaults to None.
            is_active (bool, optional): parameter if new version is active
        """

        self.counts.append(0)
        self.values.append(0.0)
        self.n_arms += 1

        if version_id is None:
            # add version as sting of n_arms if not defined
            version_id = str(self.n_arms)

        self.version_ids.append(version_id)
        self.__version_to_index[version_id] = self.n_arms - 1

        if is_active:
            self.activate_arm(self.n_arms - 1)

    def activate_arm(self, index):
        """ Make inactive (or active) version active

        Args:
            index (int): index of the arm
        """
        assert index < self.n_arms
        self.active_arms.add(index)

    def activate_version(self, version_id):
        """ Activate MAB arm with id as version_id

        Args:
            version_id (str): Version id to make active. Defaults
        """
        self.activate_arm(self.__version_to_index[version_id])

    def deactivate_arm(self, index):
        """ Make active (or inactive we don't through exception here) version inactive

        Args:
            index (int): index of the arm
        """
        if len(self.active_arms) > 2:
            self.active_arms.discard(index)

    def deactivate_version(self, version_id):
        """ Make active (or inactive we don't through exception here) version inactive

        Args:
            version_id (str): Version id to make active. Defaults
        """
        self.deactivate_arm(self.__version_to_index[version_id])

    def version_id_index(self, version_id):
        """ Return index of the version_id

        Args:
            version_id (str): Return index of the version_id
        """
        return self.__version_to_index[version_id]

    def sync_settings(self, mab_settings: dict):
        """ Syncornize MAB with external settings
            for now is update if new arms in settings or if any arm became active or not active

        Args:
            mab_settings (dict): [description]
        """

        active_versions = mab_settings["active_versions"]

        # update new versions is not found
        for i, v in enumerate(active_versions):
            if v not in self.version_ids:
                self.version_ids.append(v)
                self.__version_to_index[v] = self.n_arms
                self.n_arms += 1

        # rewrite active arms
        self.active_arms = {self.__version_to_index[v] for v in active_versions}

    def active_versions(self):
        return [self.version_ids[a] for a in self.active_arms]
